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

if display_output:
    from IPython.display import display, clear_output
    
    

# ## 3. Allow Video Upload:

if len(sys.argv) > 1:
    video_file_path = sys.argv[1]
else:
    video_file_path = "test video.mp4"  # default path

# Checking if the file exists and printing its size:
if os.path.exists(video_file_path):
    file_size = os.path.getsize(video_file_path) / (1024 * 1024)  # Convert bytes to MB
    if display_output: print(f"Loaded video file '{video_file_path}' with size: {file_size:.2f} MB successfully.")
else:
    if display_output: print(f"Video file '{video_file_path}' not found!")
    
    

# ## 4. Modify Video Length to Account for Minor Inconsistencies:

video_filename = sys.argv[1] if len(sys.argv) > 1 else "test video.mp4"
output_video_path = "output_video.mp4"  # Output video file name

desired_duration = 126.39
 

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
        
    print(np.shape(filtered_img))
    return [filtered_img]

def standard_deviation(values):
    u = np.mean(values)
    n = len(values)
    sum = 0
    for i in values:
        sum+=(pow(i-u, 2)/n)
    return np.sqrt(sum)

def get_coordinates(captured_indexes, turn_end_indexes, turn_directions, starting_direction, y_displacements):
        turn_index = 0
        x = 0
        y = 0
        direction = starting_direction
        directions = []
        locations = [[],[]]
        step = 0
        for i in range(0, len(captured_indexes)):
            for t in range(len(turn_end_indexes)-1, -1, -1):
                if captured_indexes[i] >= turn_end_indexes[t]:
                    turn_index = turn_end_indexes[t]
                    direction = turn_directions[t]
                    print(f'turn index: {turn_index} direction = {direction} captured index: {captured_indexes[i]}')
                    break
            last_point = np.max([turn_index, captured_indexes[i-1]])
            sample = y_displacements[last_point: captured_indexes[i]]
            if(len(sample) > 0):
                step = np.mean(sample)
            else:
                step = 0
            print(last_point, captured_indexes[i])
            print(sample)
            print(step)
            print(last_point)
            x += (captured_indexes[i] - last_point) * step * direction[0]
            y += (captured_indexes[i] - last_point) * step * direction[1]
            locations[0].append(x)
            locations[1].append(y)
            directions.append(direction)
        return [locations, directions]

def filter_frames(frames, frame_indeces, spacing):
    for i in range(0,len(frames)-1):
        if(frame_indeces[i+1] - frame_indeces[i] < spacing):
            frames[i] = []
    return [frames, frame_indeces]

def create_file(saved_file):
    if(not os.path.exists(saved_file)):
        os.mkdir(saved_file)


def capture_video(path):
    vidcap = cv2.VideoCapture(path)
    return vidcap


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

def process_pictures(path, compretion, noise_limit, normal_limit, turn_min_frames):
    
    saved_images = {'i':[], 'img':[]}
    
    vidcap = cv2.VideoCapture(path)
    img = []
    turn_indexes = []
    turn_ends = []
    all_locations = []
    smoothed_out_locations=[]
    turn_transition_indexes = []
    frame_directions = []
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
        success, img = vidcap.read()
        try:
            height, width, _ = np.shape(img)
        except:
            break
        

        resized_img = cv2.resize(img, [round(height/compretion), round(width/compretion)])
        filtered_img = masking(resized_img)[0]
        end_index = np.shape(resized_img)[0]-1
        if(count == 0):
            start_index = np.shape(resized_img)[0]-1
        
        indices = np.where(filtered_img != [0])

        start_index, lastX = get_indexes(start_index, end_index, filtered_img, lastX)

        y += direction[1]
        x += direction[0]


        smoothed_out_locations.append(((lastX + old_lastX)/2,y))
        if(old_start_index != 0):
            x_displacements['i'].append(count)
            x_displacements['v'].append((lastX + old_lastX)/2)

        y_displacements['i'].append(count)
        y_displacements['v'].append(start_index - old_start_index)

        location = (lastX,y) 
        all_locations.append(location)
        

        if(start_index != end_index and old_start_index == 0 and start_index != 0):
            location = (lastX,y)
            saved_images['i'].append(count)
            saved_images['img'].append(img)
            

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
        
        if(start_index == end_index):
            start_index = 0
        
        old2_lastX = old_lastX
        old_lastX = lastX
        old_start_index = start_index
        
        count += 1

    
    frames, frame_indeces = filter_frames(saved_images['img'], saved_images['i'], 10)
    locations, directions = get_coordinates(frame_indeces, turn_ends, [(-1,0),(0,-1),(-1,0),(0,1)],(0,1), y_displacements['v'])

    return saved_images, locations, frame_directions



# ## 7. Define the Function for Cropping the Frames to Desired Aspect Ratio:

def crop_to_aspect_ratio(frame, target_aspect_ratio):
    # Ensuring the frame is not None:
    if frame is None:
        raise ValueError("Frame is None. Please provide a valid frame.")

    frame_height, frame_width, _ = frame.shape
    frame_aspect_ratio = frame_width / frame_height

    if frame_aspect_ratio > target_aspect_ratio:
        new_width = int(frame_height * target_aspect_ratio)
        offset = (frame_width - new_width) // 2
        cropped_frame = frame[:, offset:offset+new_width]
    else:
        new_height = int(frame_width / target_aspect_ratio)
        offset = (frame_height - new_height) // 2
        cropped_frame = frame[offset:offset+new_height, :]

    return cropped_frame

if display_output: print("Function 'crop_to_aspect_ratio' defined successfully.")



# ## 8. Set Given Data and Calculate the Aspect Ratio:

# Given data:
vertical_length = 31.25  # in meters
horizontal_length = 33.33  # in meters
desired_aspect_ratio = horizontal_length / vertical_length

if display_output: print(f"Calculated Aspect Ratio: {desired_aspect_ratio:.2f}")



# ## 9. Calculate the Timestamps, Grab Frames, Crop Frames and Display the Results:

# Sampling timestamps for demonstration purposes (block name and timestamp in seconds):

# Grabbing frames at the desired timestamps from the modified video:
saved_images, locations, frame_directions = process_pictures('Alternative_Humans.mp4', 2, 5, 1, 10)


# Displaying cropped frames:
for img in saved_images['img']:
    if display_output:
        plt.imshow(cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        if display_output: plt.show()
        
        

# ## 10. Define the Human Detection Function:

# Initializing global counter for total humans detected across all images:
total_detected_humans = 0

def detect_humans(image):
    global total_detected_humans  # Declare the global variable to modify it

    # Converting the image from BGR to HSV:
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Defining the color range for red/orange/yellow:
    lower_red_1 = np.array([0, 100, 100])
    upper_red_1 = np.array([10, 255, 255])
    lower_red_2 = np.array([160, 100, 100])
    upper_red_2 = np.array([180, 255, 255])
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([40, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
    mask2 = cv2.inRange(hsv, lower_red_2, upper_red_2)
    mask3 = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask = mask1 + mask2 + mask3

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

    # Drawing the merged bounding boxes on the image:
    for (x1, y1, x2, y2) in merged_boxes:
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Updating the total number of detected humans:
    num_detected_humans = len(merged_boxes)
    total_detected_humans += num_detected_humans

    return image, merged_boxes



# ## 11. Process and Display Detected Humans in Each Cropped Frame:

processed_frames = []
human_boxes_dict = []

for img in saved_images['img']:
    processed_frame, human_boxes = detect_humans(img)
    processed_frames.append(processed_frame)
    human_boxes_dict.append(human_boxes)
    
# Checking if humans were detected and print a message if none were found:
    if not human_boxes:
        if display_output: print(f"No humans detected")

    # Displaying processed frame:
    if processed_frame is not None and isinstance(processed_frame, np.ndarray) and display_output:  
        plt.imshow(cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB))
        plt.title(f'Humans detected in {block}:')
        plt.axis('off')
        if display_output: plt.show()

    if display_output: print(f"Bounding boxes for {block}: {human_boxes}")
    
    

# ## 12. Print Total Number of Humans Detected Across Entire Map:

original_detected_humans = total_detected_humans
if display_output: print(f"Total number of humans: {total_detected_humans}")



# ## 13. Calculate Entire Map's Dimensions:
x_span = [location[0] for location in locations]
y_span = [locations[1] for location in locations]
max_x = np.max(x_span)
min_x = np.min(x_span)
max_y = np.max(y_span)
min_y = np.min(y_span)
total_width = [max_x - min_x]
total_height = [max_y - min_y]
x_offset = 0-min_x
y_offset = 0-min_y


if display_output: print(f"Map dimensions: Width = {total_width} pixels, Height = {total_height} pixels")



# ## 14. Reconstruct Entire Map and Convert Bounding Box Coordinates:

map_image = np.zeros((total_height, total_width, 3), dtype=np.uint8)

block_width = next(iter(cropped_frames.values())).shape[1]
block_height = next(iter(cropped_frames.values())).shape[0]

global_bboxes = []
#Use location and directions instead of offset, Flip or Transpose according to direction 
for i in range(saved_images['img']):
    processed_frame, local_bboxes = detect_humans(saved_images['img'][i])
    direction = frame_directions[i]
    map_image[y_offset*block_height:(y_offset+1)*block_height, x_offset*block_width:(x_offset+1)*block_width] = processed_frame
    for (x, y, x2, y2) in local_bboxes:
        global_x1 = x + x_offset * block_width
        global_y1 = y + y_offset * block_height
        global_x2 = x2 + x_offset * block_width
        global_y2 = y2 + y_offset * block_height
        global_bboxes.append((global_x1, global_y1, global_x2, global_y2))

for idx, (x1, y1, x2, y2) in enumerate(global_bboxes):
    cv2.rectangle(map_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    label = str(idx + 1)
    text_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_COMPLEX, 5, 2)[0]
    label_position = (x1, y1 - text_size[1] - 5)
    cv2.putText(map_image, label, label_position, cv2.FONT_HERSHEY_COMPLEX, 5, (0, 255, 0), 2, cv2.LINE_AA)

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
    for idx, (x1, y1, _, _) in enumerate(global_bboxes):
        print(f"Human {idx + 1} detected with global pixel coordinates: ({x1}, {y1}).")
else:
    # If running externally (e.g., from the C# application), write to a file
    with open(output_text_path, 'w') as f:
        for idx, (x1, y1, _, _) in enumerate(global_bboxes):
            f.write(f"Human {idx + 1} detected with global pixel coordinates: ({x1}, {y1}).\n")