from imutils import paths
import os
import shutil

# Methods
def organize_files(imagePaths):
    
    # Create a folder where the pictures are relocated
    # This is to get the directory that the program is currently running in.
    dir_path = os.path.dirname(os.path.realpath(__file__))
    folder_found = False
    for dirs in os.walk(dir_path):
        if dirs == "Curves_organized":
            folder_found = True
            break
    if folder_found == False:
        os.mkdir("Curves_organized")

    # Organize the different pictures by name
    for imagePath in imagePaths:
        # Extract the filename
        path_split = imagePath.split(os.path.sep)
        filename = path_split[2]
        # Extract the different elements
        elements = filename.split('.')
        root = elements[0]
        extension = elements[1]
        # Get the last 10 characters
        name = root[:10]
        # Remove the charater ']'
        name = name.replace("]", "")
        # Check if there is a folder with that name otherwise create it
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path += os.path.sep + "Curves_organized" + os.path.sep + name
        if check_folder_name(name) is False:
            os.mkdir(dir_path)
        
        # Copy the file
        shutil.copyfile(imagePath, dir_path)
        

# Check if the folder already exists
def check_folder_name(folder_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path += os.path.sep + "Curves"
    found = False
    for dirs in os.walk(dir_path):
        if dirs == folder_name:
            found = True
    return found

# Main flow
if not os.listdir("Curves_experiments"):
    print("Directory is empty")
else:
    print("Loading the images")
    imagePaths = list(paths.list_images("Curves_experiments"))
    # Iterate the image paths
    organize_files(imagePaths)
    print("Sucessfully finished")




        
     