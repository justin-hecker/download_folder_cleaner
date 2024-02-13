import os
import shutil

def main():
    # list to keep all image extensions
    image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    
    # navigate to downloads folder 
    os.chdir("D:\Downloads")
   
    # list files in folder and save in list
    all_files = os.listdir()
    image_files_to_move = []
    
    # iterate over all files in directory and identify image files as specified in extensions above and save those in a list
    for file in all_files:
        filename, extension = os.path.splitext(file)
        if extension.lower() in image_extensions:
            image_files_to_move.append(file)
    
    # new folder to move files to
    destination_folder = r"D:\Bilder\everything"
    
    # Move files to the new folder 
    for file in image_files_to_move:
        source_path = os.path.join(os.getcwd(), file)
        destination_path = os.path.join(destination_folder, file)
    
        # Check if the file already exists in the destination folder
        if os.path.exists(destination_path):
            # If a file with the same name already exists, rename the file before moving
            filename, extension = os.path.splitext(file)
            new_file = filename + "_duplicate" + extension
            destination_path = os.path.join(destination_folder, new_file)
            shutil.move(source_path, destination_path)
            print(f"Moved '{file}' to '{destination_folder}' as '{new_file}'")
        # if no file with same name exists, move file
        else:
            shutil.move(source_path, destination_path)
            print(f"Moved '{file}' to '{destination_folder}'")
    
    print("Image files have been moved successfully")
    input("Press enter to exit;")
        
    
if __name__ == "__main__":
    main()
