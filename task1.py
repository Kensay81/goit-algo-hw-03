import os
import shutil
import argparse

def copy_files(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        
        if os.path.isdir(item_path):
            copy_files(item_path, dest_dir)
        else:
            file_extension = os.path.splitext(item)[1]  
            subdir_path = os.path.join(dest_dir, file_extension[1:])  
            
            if not os.path.exists(subdir_path):
                os.makedirs(subdir_path)
 
            shutil.copy(item_path, subdir_path)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Copy files from source directory to destination directory and sort them by extension.")
    parser.add_argument("source_dir", help="Source directory path")
    parser.add_argument("dest_dir", nargs="?", default="dist", help="Destination directory path (default is 'dist')")
    args = parser.parse_args()

 
    try:
        copy_files(args.source_dir, args.dest_dir)
        print("Files copied and sorted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
