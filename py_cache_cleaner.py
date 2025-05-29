import os
import shutil

def cleaner_function(root,dir_name):
    pycache_path = os.path.join(root, dir_name)
    try:
        shutil.rmtree(pycache_path)
        print(f"Deleted: {pycache_path}")
    except Exception as e:
        print(f"Failed to delete {pycache_path}: {e}")

def delete_pycache_folders(directory):
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                cleaner_function(root,dir_name)

if __name__ == "__main__":
    current_dir = os.getcwd()
    print(f"Cleaning __pycache__ folders from: {current_dir}")
    delete_pycache_folders(current_dir)
    print("Cleanup complete!")
