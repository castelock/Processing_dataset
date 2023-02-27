from imutils import paths
import os
import shutil

# Methods
def organize_files(imagePaths):
    
    # Create a folder where the pictures are relocated
    # This is to get the directory that the program is currently running in.
    dir_path = os.path.dirname(os.path.realpath(__file__))
    folder_found = False
    for root, dirs, files in os.walk(dir_path):
        for dir in dirs:
            if dir == "Curves_organized":
                folder_found = True
                break
    if folder_found == False:
        os.mkdir("Curves_organized")

    # Organize the different pictures by name
    for imagePath in imagePaths:
        # Extract the filename
        path_split = imagePath.split(os.path.sep)
        filename = path_split[1]
        # Extract the different elements
        elements = filename.split('.')
        root = elements[0]
        extension = elements[1]
        # Remove white spaces
        root = root.replace(" ","")
        # Get the last 10 characters
        name = root[len(root)-11:]
        # Check if there is a folder with that name otherwise create it
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path += os.path.sep + "Curves_organized" + os.path.sep + name
        folder_searched = "Curves_organized"
        found = check_folder_name(folder_searched, name)
        if  found == False:
            os.mkdir(dir_path)
        
        # Copy the file
        file = dir_path + os.path.sep + filename
        shutil.copyfile(imagePath, file)
        

# Check if the folder already exists
# folder_searched is the folder where we are going to check if the folder is already created.
# folder_name is the name of the folder that we want to check if it has been created previously.
def check_folder_name(folder_searched,folder_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path += os.path.sep + folder_searched
    found = False
    for root, dirs, files in os.walk(dir_path):
        for dir in dirs:
            if dir == folder_name:
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




        
     