from imutils import paths
import numpy as np
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


# Rename the images
# YOU CAN PUT THE FOLDERS WITH THE IMAGES THEY ARE RENAMED AUTOMATICALLY
if not os.listdir("Gestures"):
    print("Directory is empty")
else:
    print("Loading the images")
    imagePaths = list(paths.list_images("Gestures"))
    # Sort files
    imagePaths_sorted = sorted(imagePaths)
    # Iterate the image paths
    rename_files(imagePaths_sorted, 0)
    print("Sucessfully finished")


