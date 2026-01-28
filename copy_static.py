import os
import shutil

def copy_recursive_directory(src, dest):
    """
    Recursively copies all files and directories from src to dest.
    Deletes dest first if it already exists to ensure a clean copy.
    Logs each file/directory copied for debugging.
    """
    if not os.path.exists(src):
        raise FileNotFoundError(f"Source directory does not exist: {src}")

    # Delete destination if it exists
    if os.path.exists(dest):
        if os.path.isdir(dest):
            shutil.rmtree(dest)
        else:
            os.remove(dest)  # unlikely, but just in case

    # Create destination directory
    os.makedirs(dest, exist_ok=True)

    # Loop through all items in the source directory
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            print(f"Copying file: {src_path}")
            shutil.copy2(src_path, dest_path)  # copy2 preserves metadata
        elif os.path.isdir(src_path):
            print(f"Entering directory: {src_path}")
            copy_recursive_directory(src_path, dest_path)
