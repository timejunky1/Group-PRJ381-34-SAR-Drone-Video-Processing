# ## 0. Set display behavior based on environment context:

import os

# Default is to display
display_output = True

if os.getenv('CONTEXT') == 'APP':
    display_output = False
    
    

# ## 1. Install Libraries:

import subprocess

def install_package(package_name, pip_name=None):
    """Installs the given package using pip."""
    if pip_name is None:
        pip_name = package_name
    subprocess.run(['python', '-m', 'pip', 'install', pip_name])

try:
    import cv2
except ImportError:
    install_package('cv2', 'opencv-python')

try:
    import cv2  
except ImportError:
    install_package('cv2', 'opencv-python-headless')

try:
    import matplotlib  
except ImportError:
    install_package('matplotlib')

try:
    import tensorflow  
except ImportError:
    install_package('tensorflow')

try:
    import pickle  
except ImportError:
    install_package('pickle')


try:
    import IPython  
except ImportError:
    install_package('IPython')
    
    

# ## 2. Import Libraries:

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
import sys
import json
import pickle
import tensorflow as tf
from tensorflow import keras

if display_output:
    from IPython.display import display, clear_output
    
    

# ## 3. Allow Video Upload:

if len(sys.argv) > 1:
    video_file_path = sys.argv[1]
    useModel = sys.argv[2]
else:
    video_file_path = "Alternative_Only_Humans.mp4"  # default path

useModel = False

# Checking if the file exists and printing its size:
if os.path.exists(video_file_path):
    file_size = os.path.getsize(video_file_path) / (1024 * 1024)  # Convert bytes to MB
    if display_output: print(f"Loaded video file '{video_file_path}' with size: {file_size:.2f} MB successfully.")
else:
    if display_output: print(f"Video file '{video_file_path}' not found!")
    
    

# ## 4. Modify Video Length to Account for Minor Inconsistencies:

video_filename = sys.argv[1] if len(sys.argv) > 1 else "test video.mp4"
output_video_path = "output_video.mp4"  # Output video file name

# ## 6. Capture Nessesary frames:
def masking(img):
    #Image Colour Conversion
    try:
        rbg_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        hsv_img = cv2.cvtColor(rbg_img, cv2.COLOR_RGB2HSV)
        lower = np.array([0, 150, 50])
        upper = np.array([35, 255, 255])
        mask = cv2.inRange(hsv_img, lower, upper)
        filtered_img = cv2.bitwise_and(rbg_img, rbg_img, mask=mask)
    except:
        filtered_img = img
        print("Problem")
        
    return [filtered_img]

def standard_deviation(values):
    u = np.mean(values)
    n = len(values)
    sum = 0
    for i in values:
        sum+=(pow(i-u, 2)/n)
    return np.sqrt(sum)

def get_equation_value_at_x(x, m, b):
    return m*x+b

def reject_outliers(data):
    removed_indexes = []
    result = []
    n = len(data)
    x = [i for i in range(0, n)]
    if(n>2):
        xy = [x[i] * data[i] for i in range(0, n)]
        x_2 = [np.power(i, 2) for i in x]
        m =  ((n*np.sum(xy))-(np.sum(x)*np.sum(data)))/(n*np.sum(x_2)-np.power(np.sum(x),2))
        b = (np.sum(data)-m*np.sum(x))/n
        sd = standard_deviation(data)
        for i in range(0, len(data)):
            if abs(data[i]-get_equation_value_at_x(x[i], m, b))<sd/4:
                result.append(data[i])
            else:
                removed_indexes.append(i)
                
        best_fit = [get_equation_value_at_x(x_, m, b) for x_ in x]
    else:
        for i in range(0, len(data)):
            if data[i] !=0:
                result.append(data[i])
            else:
                removed_indexes.append(i)
        best_fit = data
    f_x = [x for x in x if x not in removed_indexes]

    return result, x, f_x, best_fit,

def get_coordinates(captured_indexes, turn_end_indexes, turn_directions, starting_direction, y_displacements, compretion, height, width):
        turn_index = 0
        x = round(width/2)
        y = round(height/2)
        direction = starting_direction
        directions = []
        locations = []
        step = 0
        if(display == True):
            plt.figure(figsize=(10,15))

        for i in range(0, len(captured_indexes)):
            for t in range(len(turn_end_indexes)-1, -1, -1):
                if captured_indexes[i] >= turn_end_indexes[t]:
                    turn_index = turn_end_indexes[t]
                    direction = turn_directions[t]
                    print(f'turn index: {turn_index} direction = {direction} captured index: {captured_indexes[i]}')
                    break
            last_point = np.max([turn_index, captured_indexes[i-1]])
            sample = y_displacements[last_point: captured_indexes[i]]
            smoothed_sample, xs, f_x, best_fit  = reject_outliers(sample)

            if(display == True):
                plt.subplot(5,5,i+1)
                plt.title(f"{direction}")
                plt.plot(xs, sample)
                plt.scatter(xs, sample)
                plt.plot(f_x, smoothed_sample)
                plt.scatter(f_x, smoothed_sample)
                plt.plot(xs, best_fit)

            if(len(smoothed_sample) > 0):
                step = np.mean(smoothed_sample)*compretion
                
                
            x += (captured_indexes[i] - last_point) * step * direction[0]
            y += (captured_indexes[i] - last_point) * step * direction[1]
            print(f"Step: {step}")
            print(x,y)
            #x+=np.sum(smoothed_sample) * direction[0] * compretion
            #y+=np.sum(smoothed_sample) * direction[1] * compretion
            locations.append((x,y))
            directions.append(direction)
            
        if(display == True):    
            plt.show()

        return [locations, directions]

def filter_frames(frames, frame_indeces, locations, directions, spacing):
    for i in range(1,len(frames)):
        if(frame_indeces[i] - frame_indeces[i-1] < spacing and len(frames[i-1])>0):
            frames[i] = []
    
    #filtering out empties
    directions = [directions[i] for i in range(0,len(frames)) if len(frames[i]) > 0]
    locations = [locations[i] for i in range(0,len(frames)) if len(frames[i]) > 0]
    frames = [frame for frame in frames if len(frame) > 0]


    return [frames, locations, directions]

def create_file(saved_file):
    if(not os.path.exists(saved_file)):
        os.mkdir(saved_file)

def calculate_pixel(resized_img):
    #Pixel Calculation
    success = False
    instances_count = 0
    try:
        indices = np.where(resized_img != [0])
    
    except:
        success = False
            
    return [indices]

def get_indexes(start_index, end_index, resized_img, lastX):
    width = np.size(resized_img, 1)
    lastX = lastX

    for i in range(start_index,end_index+1, 1):
        start_index = i
        if(np.max(resized_img[i])):
                break
    else:
        return [start_index, lastX]
        
    for i in range(0, width-1, 1):
        if(resized_img[start_index][i].any() != 0):#Faulty x lingers on a value
            lastX = i
            break
            
    return [start_index, lastX]


def process_pictures(path, compretion, noise_limit, normal_limit, turn_min_frames, turn_directions):
    
    img = []
    saved_images = {'i':[], 'img':[]}
    height = 0
    width = 0
    displacement = 0
    vidcap = cv2.VideoCapture(path)
    turn_indexes = []
    turn_ends = []
    all_locations = []
    smoothed_out_locations=[]
    turn_transition_indexes = []
    success = True
    count = 0
    start_index = 0
    lastX = 0
    x = 0
    y = 0
    old_lastX = 0
    old_start_index = 0
    old2_lastX = 0
    direction = (0,1)
    y_displacements = {'i': [], 'v': []}
    x_displacements = {'i': [], 'v': []}
    while success: 
        last_img = img
        success, img = vidcap.read()
        #saving the last successful picture
        if(not success):
            location = (lastX,y) 
            all_locations.append(location)
            saved_images['i'].append(count)
            saved_images['img'].append(last_img)
        try:
            height, width, _ = np.shape(img)
        except:
            break
        
        #Resizing the picture and getting aray of the indices of the instances using a mask
        resized_img = cv2.resize(img, [round(height/compretion), round(width/compretion)])
        filtered_img = masking(resized_img)[0]
        end_index = np.shape(resized_img)[0]-1
        if(count == 0):
            start_index = np.shape(resized_img)[0]-1
        
        indices = np.where(filtered_img != [0])

        #calling the method for keeping track of the index and therefor keeping track of the movement of the drone
        start_index, lastX = get_indexes(start_index, end_index, filtered_img, lastX)

        y += direction[1]
        x += direction[0]


        smoothed_out_locations.append(((lastX + old_lastX)/2,y))
        #allocating the deplacements to a string for use in determining turns
        if(old_start_index != 0):
            x_displacements['i'].append(count)
            x_displacements['v'].append((lastX + old_lastX)/2)
        
        if(old_start_index != 0 and start_index != end_index):
            displacement = start_index - old_start_index
            y_displacements['i'].append(count)
            y_displacements['v'].append(displacement)
        else:
            y_displacements['i'].append(count)
            y_displacements['v'].append(displacement)

        location = (lastX,y) 
        all_locations.append(location)
        

        if(start_index != end_index and old_start_index == 0 and start_index != 0):
            location = (lastX,y)
            saved_images['i'].append(count)
            saved_images['img'].append(img)
            
        #determine under conditions regarding the standard deviation of the past indexes if the drone has turned or not
        if(standard_deviation([lastX, old_lastX, old2_lastX]) < normal_limit):
            if(len(x_displacements['v']) > 1):
                x_displacements['v'].remove(np.max(x_displacements['v']))
            std = standard_deviation(x_displacements['v'])
            if(abs(std) > noise_limit and len(x_displacements['i']) > turn_min_frames):
                turn_transition_indexes.append(x_displacements['i'][0])
                turn_transition_indexes.append(x_displacements['i'][-1])
                turn_ends.append(x_displacements['i'][-1])
                for i in x_displacements['i']:
                    turn_indexes.append(i)
                cut_index = 0
                for i in range (len(saved_images['i'])-1, 0, -1):
                    if(saved_images['i'][i] < x_displacements['i'][0]):
                        cut_index = i + 1
                        break
                
                saved_images['i'] = saved_images['i'][0:cut_index]
                saved_images['img'] = saved_images['img'][0:cut_index]
                saved_images['i'].append(x_displacements['i'][0])
                saved_images['img'].append([])
                saved_images['i'].append(x_displacements['i'][-1])
                saved_images['img'].append([])
                start_index = 0
            x_displacements['i'] = []
            x_displacements['v'] = []
            location = (lastX,y)
        
        #resets the index if it has come to the end
        if(start_index == end_index):
            start_index = 0
        
        old2_lastX = old_lastX
        old_lastX = lastX
        old_start_index = start_index
        
        count += 1

    if(display_output):
        plt.figure(figsize=(10,100))
        xs = []
        ys = []
        for i in range(0, len(all_locations)):
            xs.append(all_locations[i][0])
            ys.append(all_locations[i][1])
        plt.plot(xs,ys)
        plt.scatter(xs,ys)
        xs = []
        ys = []
        for i in range(0, len(smoothed_out_locations)):
            xs.append(smoothed_out_locations[i][0])
            ys.append(smoothed_out_locations[i][1])
        plt.plot(xs,ys,)
        plt.scatter(xs,ys)
        xs = []
        ys = []
        for i in turn_indexes:
            xs.append(all_locations[i][0])
            ys.append(all_locations[i][1])
        plt.scatter(xs,ys)
        print(len(xs))
        print(len(ys))
        xs = []
        ys = []
        for i in saved_images['i']:
            xs.append(all_locations[i][0])
            ys.append(all_locations[i][1])
        plt.plot(xs,ys)
        xs = []
        ys = []
        for i in turn_transition_indexes:
            xs.append(smoothed_out_locations[i][0])
            ys.append(smoothed_out_locations[i][1])
        plt.plot(xs,ys)
        plt.scatter(xs,ys)
        plt.show
    
    locations, directions = get_coordinates(saved_images['i'], turn_ends, turn_directions[1:],turn_directions[0], y_displacements['v'], compretion, height, width)

    if(display_output == True):
        plt.figure(figsize=(10,20))
        xs = [l[0] for l in locations]
        ys = [l[1] for l in locations]
        plt.scatter(xs, ys)
        plt.plot(xs, ys)

    frames, locations, directions = filter_frames(saved_images['img'], saved_images['i'], locations, directions, 10)

    if(display_output == True):
        xs = [l[0] for l in locations]
        ys = [l[1] for l in locations]
        plt.scatter(xs, ys)
        plt.show()

    return width, height, frames, locations, directions

#fetching the flight directions from a file or initialising it to a default
turn_directions = []
try:
    with open("directions.txt") as file:
        for line in file.readlines():
            turn_directions.append(line.strip()[1,-2])

    flight_directions = [d.split(",") for d in turn_directions]
    flight_directions = [(d[0],d[1]) for d in flight_directions]

except:
    flight_directions = [(0,1),(-1,0),(0,-1),(-1,0),(0,1)]

width, height, captured_frames, locations, frame_directions = process_pictures('Alternative_Only_Humans.mp4', 2, 5, 1, 8,flight_directions)


# Displaying cropped frames:
for img in captured_frames:
    if display_output:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        if display_output: plt.show()
        
        

# ## 10. Define the Human Detection Function:

# Initializing global counter for total humans detected across all images:
total_detected_humans = 0

#fetching human detection model
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except:
    print("Can not load machine learning model")
    useModel = False

def Predict(img):
    class_names = ['Human', 'Non Human']
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    
    identification = class_names[np.argmax(score)]
    
    return(identification)

def cropping(x, y, width, height, sectioningRatio, cropSize, img, count):
    
    addition = 0
    
    location = (x, y)
    dist =np.max([height, width])
    
    if(dist < cropSize):
        addition = round((cropSize-dist)/2)
    
    maxY = (location[1] + dist)
    minY = (location[1])
    maxX = (location[0] + dist)
    minX = (location[0])          
                
    maxY = maxY*sectioningRatio+addition
    minY = minY*sectioningRatio-addition
    maxX = maxX*sectioningRatio+addition
    minX = minX*sectioningRatio-addition
    
    croppedImg = img[minY: maxY,minX: maxX]
    croppedImg = cv2.resize(croppedImg, (363, 363))
    
    return croppedImg

def detect_humans(image):
    global total_detected_humans  # Declare the global variable to modify it

    # Converting the image from BGR to HSV:
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Defining the color range for red/orange/yellow:
    lower = np.array([0, 150, 50])
    upper = np.array([35, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)

    # Using morphology to remove noise:
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.dilate(mask, kernel, iterations=2)

    # Finding contours:
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    bounding_boxes = []

    for contour in contours:
        if cv2.contourArea(contour) > 200:
            (x, y, w, h) = cv2.boundingRect(contour)
            bounding_boxes.append((x, y, x+w, y+h))
            

   # Calculating the average width and height for adaptive merging:
    if len(bounding_boxes) > 0:
        avg_width = sum([x2 - x1 for x1, _, x2, _ in bounding_boxes]) / len(bounding_boxes)
        avg_height = sum([y2 - y1 for _, y1, _, y2 in bounding_boxes]) / len(bounding_boxes)
    else:
        avg_width = 0
        avg_height = 0

    # Merging overlapping or close boxes:
    results = []
    merged_boxes = []

    for i, (x1, y1, x2, y2) in enumerate(bounding_boxes):
        merged = False
        for j, (x3, y3, x4, y4) in enumerate(merged_boxes):
            EXTENDED_MARGIN = max(avg_width, avg_height)  # Making margin based on average width and height
            x1_adj, y1_adj = x1 - EXTENDED_MARGIN, y1 - EXTENDED_MARGIN
            x2_adj, y2_adj = x2 + EXTENDED_MARGIN, y2 + EXTENDED_MARGIN
            if x1_adj < x4 and x2_adj > x3 and y1_adj < y4 and y2_adj > y3:
                x = min(x1, x3)
                y = min(y1, y3)
                w = max(x2, x4)
                h = max(y2, y4)

                merged_boxes[j] = (x, y, w, h)
                merged = True
                break

        if not merged:
            merged_boxes.append((x1, y1, x2, y2))
    
    #If it is specified to use machine learning model. A cropped section of the image will be sent to the model for recognition
    if(useModel == True):
        filtered_img = masking(image)
        for j, (x, y, w, h) in enumerate(merged_boxes):
            cropped_image = cropping(x, y, w, h, 1, 100, filtered_img)
            result = Predict(cropped_image)
            if(result == "Human"):
                results.append((x, y, w, h))
    else:
        results = merged_boxes

    # Drawing the merged bounding boxes on the image:
    for (x1, y1, x2, y2) in results:
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Updating the total number of detected humans:
    num_detected_humans = len(merged_boxes)
    total_detected_humans += num_detected_humans

    return image, results



# ## 11. Process and Display Detected Humans in Each Cropped Frame:

processed_frames = []
human_boxes_dict = []

# ## 12. Print Total Number of Humans Detected Across Entire Map:

original_detected_humans = total_detected_humans
if display_output: print(f"Total number of humans: {total_detected_humans}")



# ## 13. Calculate Entire Map's Dimensions:
x_span = [location[0] for location in locations]
y_span = [location[1] for location in locations]
max_x = round(np.max(x_span) + np.max([width/2, height/2]))
min_x = round(np.min(x_span) - np.max([width/2, height/2]))
max_y = round(np.max(y_span) + np.max([width/2, height/2]))
min_y = round(np.min(y_span) - np.max([width/2, height/2]))
total_width = round(max_x - min_x)
total_height = round(max_y - min_y)
x_offset = 0-min_x
y_offset = 0-min_y

global_locations = []
map_image = np.zeros((total_height, total_width, 3), dtype=np.uint8)


if display_output: print(f"Map dimensions: Width = {total_width} pixels, Height = {total_height} pixels")

#define the draw section function which has to do with transposing the picture if necessary
def draw_section(img, fx, fy, direction):
    top_right_x = round(fx+(direction[1]*(round(width/2)) + direction[0]*(round(height/2))))
    top_right_y = round(fy+(-direction[0]*(round(width/2)) + direction[1]*(round(height/2))))
    print(f"Cordinates of top right: {top_right_x, top_right_y}")
    top_right_x += x_offset
    top_right_y += y_offset
    print(f"Pluss offsets: {top_right_x, top_right_y}")
    print(f"Ordered Y: {total_height-top_right_y}")
    top_right_y = total_height-top_right_y
    if(direction == (0,1)):
        y1 = top_right_y
        y2 = top_right_y+height
        x1 = top_right_x-width
        x2 = top_right_x
        print(y1,y2,x1,x2)
        map_image[y1:y2, x1: x2] = img
    if(direction == (1,0)):
        y1 = top_right_y-width
        y2 = top_right_y
        x1 = top_right_x-height
        x2 = top_right_x
        print(y1,y2,x1,x2)
        reconstructed_img = np.zeros((width, height, 3), dtype=np.uint8)
        for y in range(0, height):
            for x in range(0, width):
                reconstructed_img[x][height-y-1] = img[y][x]

        map_image[y1:y2, x1:x2] = reconstructed_img
    if(direction == (0,-1)):
        y1 = top_right_y-height
        y2 = top_right_y
        x1 = top_right_x
        x2 = top_right_x+width
        print(y1,y2,x1,x2)
        reconstructed_img = np.zeros((height, width, 3), dtype=np.uint8)
        for y in range(0, height):
            for x in range(0, width):
                reconstructed_img[height-y-1][width-x-1] = img[y][x]

        map_image[y1:y2, x1:x2] = reconstructed_img
    if(direction == (-1,0)):
        y1 = top_right_y
        y2 = top_right_y+width
        x1 = top_right_x
        x2 = top_right_x+height
        print(y1,y2,x1,x2)
        reconstructed_img = np.zeros((width, height, 3), dtype=np.uint8)
        for y in range(0, height):
            for x in range(0, width):
                reconstructed_img[width-x-1][y] = img[y][x]

        map_image[y1:y2, x1:x2] = reconstructed_img

#calculating global locations
for i in range(0, len(captured_frames)):
    f_locations = []
    processed_frame, local_bboxes = detect_humans(captured_frames[i])
    direction = frame_directions[i]
    cx = width/2
    cy = height/2
    fx = locations[i][0]
    fy = locations[i][1]
    for (x, y, x2, y2) in local_bboxes:
        x = round((x+x2)/2)
        y = round((y+y2)/2)
        g_x = round(fx+(direction[1]*(x-cx) - direction[0]*(y-cy)))
        g_y = round(fy+(-direction[0]*(x-cx) + -direction[1]*(y-cy)))
        global_locations.append((g_x,g_y))

    ##drawwing processed frame on global picture
    draw_section(processed_frame, fx, fy, direction)

for i in range(0, len(global_locations)):
    label = str(i+1)
    text_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_COMPLEX, 5, 2)[0]
    label_position = (round(global_locations[i][0] + x_offset), total_height-(round(global_locations[i][1] + y_offset)))
    cv2.putText(map_image, label, label_position, cv2.FONT_HERSHEY_COMPLEX, 5, (0, 255, 0), 2, cv2.LINE_AA)

# ## 14. Reconstruct Entire Map and Convert Bounding Box Coordinates:

output_image_path = "humanMap.jpg"
cv2.imwrite(output_image_path, map_image)

if display_output:
    plt.figure(figsize=(total_width/100, total_height/100))
    plt.imshow(cv2.cvtColor(map_image, cv2.COLOR_BGR2RGB), interpolation='none')
    plt.title('Global Map with Human Detections:', fontsize=29)
    plt.axis('off')
    if display_output: plt.show()

# Defining the path for the output text file:
output_text_path = "locations.txt"

if 'external' not in sys.argv:
    # If running in Jupyter, print the output
    for i, (x,y) in enumerate(global_locations):
        print(f"Human {i + 1} detected with global pixel coordinates: ({x}, {y}).")
else:
    # If running externally (e.g., from the C# application), write to a file
    with open(output_text_path, 'w') as f:
        for i, (x,y) in enumerate(global_locations):
            f.write(f"Human {i + 1} detected with global pixel coordinates: ({x}, {y}).\n")