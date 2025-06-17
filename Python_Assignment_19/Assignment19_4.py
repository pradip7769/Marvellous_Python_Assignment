# Q4. Design automation script which accept two directory names and one file extension. 
# Copy all files with the specified extension from first directory into second directory.
# Second directory should be created at run time. 
# Usage : DirectoryCopyExt.py "Demo" "Temp" ".exe"
# Demo is name of directory which is existing and contains files in it.
# We have to create new Directory as Temp and copy all files with extension .exe form Demo to Temp.


import os
import sys
import shutil

def copy_files_with_extension():
   
    source_dir = os.path.abspath(sys.argv[1])
    dest_dir = os.path.abspath(sys.argv[2])
    file_ext = sys.argv[3]

    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    if not os.path.isdir(source_dir):
        print(f"'{source_dir}' is not a valid directory.")
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created destination directory: {dest_dir}")
    else:
        print(f"Destination directory already exists: {dest_dir}")

    for filename in os.listdir(source_dir):
        if filename.endswith(file_ext):
            src_file = os.path.join(source_dir, filename)
            dest_file = os.path.join(dest_dir, filename)
            if os.path.isfile(src_file):
                shutil.copy2(src_file, dest_file)
                
                

def main():
    
    copy_files_with_extension()

if __name__ == "__main__":
    main()
