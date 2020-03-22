from imutils import paths
import numpy as np
import cv2
import os


# Methods
def rename_files(imagePaths, variable):
    for imagePath in imagePaths:
        # Extract the filename
        path_split = imagePath.split(os.path.sep)
        filename = path_split[2]
        # Extract the different elements
        elements = filename.split('.')
        root = elements[0]
        extension = elements[1]
        variable = variable+1
        # Create the new filename
        new_filename = str(variable) + "." + extension
        new_path = path_split[0] + os.path.sep + path_split[1] + os.path.sep + new_filename
        # Rename the file
        os.rename(imagePath, new_path)


skip = True
# Checking the folder of gestures that are individually
"""if not os.listdir("Single") or skip:
    print("Directory is empty or the user skipped this process")
else:
    print("[INFO] Loading the images when they are separately")
    imagePaths = list(paths.list_images("Single"))
    # Iterate the image paths
    rename_files(imagePaths, 10, "single")


# Checking the folder with gestures when they are merged
if not os.listdir("All"):
    print("Directory is empty")
else:
    print("[INFO] Loading the images when they are all together")
    imagePaths = list(paths.list_images("All"))
    # Iterate the image paths
    rename_files(imagePaths, 0, "all")"""

if not os.listdir("Gestures"):
    print("Directory is empty")
else:
    print("[INFO] Loading the images")
    imagePaths = list(paths.list_images("Gestures"))
    # Sort files
    imagePaths_sorted = sorted(imagePaths)
    # Iterate the image paths
    rename_files(imagePaths, 0, "all")


