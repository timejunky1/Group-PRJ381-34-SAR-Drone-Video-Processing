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
    import pickle  
except ImportError:
    install_package('pickle')

try:
    import tensorflow  
except ImportError:
    install_package('tensorflow')

try:
    import keras  
except ImportError:
    install_package('keras')

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
useModel = False
if len(sys.argv) > 1:
    video_file_path, useModel = sys.argv[1].split(",")
    if(useModel == "False"):
        useModel = False
else:
    video_file_path = "test video.mp4"  # default path

# Checking if the file exists and printing its size:
if os.path.exists(video_file_path):
    file_size = os.path.getsize(video_file_path) / (1024 * 1024)  # Convert bytes to MB
    if display_output: print(f"Loaded video file '{video_file_path}' with size: {file_size:.2f} MB successfully.")
else:
    if display_output: print(f"Video file '{video_file_path}' not found!")

display_output = True

# ## 4. Modify Video Length to Account for Minor Inconsistencies:

video_filename = sys.argv[1] if len(sys.argv) > 1 else "test video.mp4"
output_video_path = "output_video.mp4"  # Output video file name

desired_duration = 126.39

# Opening the video file:
cap = cv2.VideoCapture(video_filename)

if not cap.isOpened():
    if display_output: print(f"Error: Couldn't open the video file '{video_filename}'.")
else:
    if display_output: print(f"Video file '{video_filename}' opened successfully.")

    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    original_fps = int(cap.get(cv2.CAP_PROP_FPS))
    original_duration = video_length / original_fps

    new_fps = video_length / desired_duration

    if display_output: print(f'Original Duration: {original_duration:.2f} seconds')
    if display_output: print(f'Desired Duration: {desired_duration:.2f} seconds')
    if display_output: print(f'Original FPS: {original_fps}')
    if display_output: print(f'New FPS: {new_fps:.2f}')

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, new_fps, (int(cap.get(3)), int(cap.get(4)))) 

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

    if display_output: print(f'Processed video saved as {output_video_path} with new duration of {desired_duration:.2f} seconds')

    cap.release()
    out.release()



# ## 5. Calculate the Time Stamps at which a Frame must be Grabbed from the Video for Analysis:

def calculate_timestamps(total_time, speed, vertical_length, horizontal_length, path):
    timestamps = []
    time_elapsed = 0.0
    
    # Calculating the time for Block 1 when the drone is in the middle of the block:
    time_elapsed += (vertical_length / 2) / speed
    timestamps.append((f'Block {path[0]}', round(time_elapsed, 2)))

    for i in range(len(path)-1):
        current_block = path[i]
        next_block = path[i+1]
        
        if current_block // 4 == next_block // 4:  # Checking if blocks are in the same column:
            distance = vertical_length
        else:
            distance = horizontal_length
            
        time_to_next_block = distance / speed
        time_elapsed += time_to_next_block
        
        timestamps.append((f'Block {next_block}', round(time_elapsed, 2)))
        
    return timestamps

# Given constants:
total_time = 126.39  # in seconds
speed = 3.0  # in meters per second
vertical_length = 31.25  # in meters
horizontal_length = 33.33  # in meters
path = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # The order of blocks

# Calculating the timestamps:
timestamps = calculate_timestamps(total_time, speed, vertical_length, horizontal_length, path)

# Printing the timestamps:
for block, timestamp in timestamps:
    if display_output: print(f'{block}: {timestamp} seconds')
    
    

# ## 6. Define the Function for Grabbing Frames at Desired Timestamps:

def grab_frames(video_path, timestamps):
    frames = {}
    cap = cv2.VideoCapture(video_path)

    for block, timestamp in timestamps:
        frame_time = int(timestamp * 1000)  # converting to milliseconds
        cap.set(cv2.CAP_PROP_POS_MSEC, frame_time)
        ret, frame = cap.read()
        if ret:
            frames[block] = frame
        else:
            if display_output: print(f"Failed to grab frame for {block} at timestamp {timestamp}s")

    cap.release()
    if display_output: print("Frames grabbed successfully!")
    return frames

if display_output: print("Function 'grab_frames' defined successfully!")



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
timestamps = [('Block 1', 5.21), 
             ('Block 2', 15.62),
             ('Block 3', 26.04),
             ('Block 4', 37.15),
             ('Block 5', 47.57),
             ('Block 6', 57.98),
             ('Block 7', 68.4),
             ('Block 8', 79.51),
             ('Block 9', 89.93),
             ('Block 10', 100.34),
             ('Block 11', 110.76),
             ('Block 12', 121.87)]

# Grabbing frames at the desired timestamps from the modified video:
grabbed_frames = grab_frames(output_video_path, timestamps)

# Cropping each frame to match the desired aspect ratio:
cropped_frames = {block: crop_to_aspect_ratio(frame, desired_aspect_ratio) for block, frame in grabbed_frames.items()}

# Displaying cropped frames:
for block, cropped_frame in cropped_frames.items():
    if display_output:
        plt.imshow(cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2RGB))
        plt.title(f'Cropped Frame for {block}:')
        plt.axis('off')
        if display_output: plt.show()
        
        

# ## 10. Define the Human Detection Function:

# Initializing global counter for total humans detected across all images:
total_detected_humans = 0

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
        print("Problem with masking")
        
    return filtered_img

if(useModel):
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

def cropping(x, y, width, height, sectioningRatio, cropSize, img):
    
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

processed_frames = {}
human_boxes_dict = {}

for block, cropped_frame in cropped_frames.items():
    processed_frame, human_boxes = detect_humans(cropped_frame)
    processed_frames[block] = processed_frame
    human_boxes_dict[block] = human_boxes
    
# Checking if humans were detected and print a message if none were found:
    if not human_boxes:
        if display_output: print(f"No humans detected in {block}.")

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

total_width = 3 * next(iter(cropped_frames.values())).shape[1]
total_height = 4 * next(iter(cropped_frames.values())).shape[0]

if display_output: print(f"Map dimensions: Width = {total_width} pixels, Height = {total_height} pixels")



# ## 14. Reconstruct Entire Map and Convert Bounding Box Coordinates:

map_image = np.zeros((total_height, total_width, 3), dtype=np.uint8)
block_offsets = {
    'Block 1': (0, 0),
    'Block 2': (0, 1),
    'Block 3': (0, 2),
    'Block 4': (0, 3),
    'Block 5': (1, 3),
    'Block 6': (1, 2),
    'Block 7': (1, 1),
    'Block 8': (1, 0),
    'Block 9': (2, 0),
    'Block 10': (2, 1),
    'Block 11': (2, 2),
    'Block 12': (2, 3),
}

block_width = next(iter(cropped_frames.values())).shape[1]
block_height = next(iter(cropped_frames.values())).shape[0]

global_bboxes = []

for block, cropped_frame in cropped_frames.items():
    processed_frame, local_bboxes = detect_humans(cropped_frame)
    x_offset, y_offset = block_offsets[block]
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