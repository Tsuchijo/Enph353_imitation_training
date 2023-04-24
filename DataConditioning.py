import cv2
import numpy as np
import os

# iterate through all of the images in the folder and downsample them to 320X180
file_path = "/home/fizzer/353_comp_training/training_data2"
delete_list = []
def downsampleImages():
    for filename in os.listdir(file_path):
        if filename.endswith(".png"):
            twist = float(filename.split(",")[0])
            throttle = float(filename.split(",")[1])
            if (abs(throttle) < 0.05 and abs(twist) < 0.05):
                # add to delete list
                delete_list.append(filename)
            img = cv2.imread(f"/home/fizzer/353_comp_training/training_data2/{filename}")
            if img is None:
                print("Image is empty")
                continue
            else: 
                img = cv2.resize(img, (160, 90))
                cv2.imwrite(f"/home/fizzer/353_comp_training/training_data2/{filename}", img)
        else:
            continue

# iterate through all of the images in the folder and delete the ones that are not needed
def deleteImages():
    for filename in os.listdir(file_path):
        if filename.endswith(".png"):
            if filename in delete_list:
                os.remove(f"/home/fizzer/353_comp_training/training_data2/{filename}")
        else:
            continue

downsampleImages()
deleteImages()