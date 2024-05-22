import os
import shutil

def main():
    # list to keep all image extensions
    image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    setup_extensions = [".exe", ".msi"]
    zip_extensions = [".rar", ".zip"]
    
    # navigate to downloads folder 
    #dloads_folder = input("Please enter Downloads-Folder Path (example format: 'D:\Downloads'): ")
    os.chdir("D:\Downloads")
   
    # list files in folder and save in list
    all_files = os.listdir()
    image_files_to_move = []
    pdf_files_to_move = []
    
    # iterate over all files in directory and identify files as specified in extensions above and save those in a list or delete them
    for file in all_files:
        filename, extension = os.path.splitext(file)
        if extension.lower() in image_extensions:
            image_files_to_move.append(file)
        elif extension.lower() == ".pdf":
            pdf_files_to_move.append(file) 
        elif extension.lower() in setup_extensions:
            os.remove(file)
        elif extension.lower() in zip_extensions:
            os.remove(file)
    
    # new folder to move files to
    #new_folder = input("Please enter desired Path for Image files (example format: 'D:\Bilder\everything'): ")
    destination_folder = "D:\Bilder\everything"
    destination_folder_pdfs = ""
    
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
    
    for file in pdf_files_to_move:
        source_path = os.path.join(os.getcwd(), file)
        destination_path = os.path.join(destination_folder_pdfs, file)
    
        # Check if the file already exists in the destination folder
        if os.path.exists(destination_path):
            # If a file with the same name already exists, rename the file before moving
            filename, extension = os.path.splitext(file)
            new_file = filename + "_duplicate" + extension
            destination_path = os.path.join(destination_folder_pdfs, new_file)
            shutil.move(source_path, destination_path)
            print(f"Moved '{file}' to '{destination_folder_pdfs}' as '{new_file}'")
        # if no file with same name exists, move file
        else:
            shutil.move(source_path, destination_path)
            print(f"Moved '{file}' to '{destination_folder_pdfs}'")
    
    print("files have been moved successfully")
    input("Press enter to exit ")
            
if __name__ == "__main__":
    main()
