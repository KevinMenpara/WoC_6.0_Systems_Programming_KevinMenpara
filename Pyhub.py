import os
import shutil
import sys

def organize_files(directory_path):
    # Ensure the provided directory path is valid
    if not os.path.exists(directory_path):
        print(f"Entered directory  path: '{directory_path}' does not exist.")
        sys.exit(1)

    # Create a dictionary to store file extensions and their corresponding directories
    mime_directories = {}

    # Iterate through files in the specified directory
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)

        # Check if the path is a file (not a directory)
        if os.path.isfile(filepath):
            # Extract the file extension
            _, file_extension = os.path.splitext(filename)

            # Remove the leading dot from the extension
            file_extension = file_extension[1:]

            # Create a directory for the extension if not already exists
            if file_extension not in mime_directories:
                mime_directory = os.path.join(directory_path, file_extension)
                os.makedirs(mime_directory, exist_ok=True)
                mime_directories[file_extension] = mime_directory

            # Move the file to its corresponding extension directory
            new_filepath = os.path.join(mime_directories[file_extension], filename)
            shutil.move(filepath, new_filepath)
            print(f"Moved '{filename}' to '{file_extension}' directory.")

    print("File organization completed successfully.")

if __name__ == "__main__":
    path = input("Enter the directory path to organize files: ")
    organize_files(path)
