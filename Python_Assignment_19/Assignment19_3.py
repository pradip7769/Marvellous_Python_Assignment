# Q3. Design automation script which accept two directory names. Copy all files from first directory into second directory. 
# Second directory Should be created at run time. 
# Usage : DirecotyCopy.py "Demo" "Temp"

# Demo is name of directory which is existing nd contains files in it. we have to create new Directory as Temp and Copy all files from Demo to Temp.

import os
import sys
import shutil

def copy_directory_files():
    source_dir = os.path.abspath(sys.argv[1])
    dest_dir = os.path.abspath(sys.argv[2])

    if not os.path.exists(source_dir):
        print("Source directory" + source_dir + "does not exist")
        return 
    
    if not os.path.isdir(source_dir):
        print(f"'{source_dir}' is not a valid directory.")
        return 
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created destination directory : {dest_dir}")
    else:
        print(f"Destination directory already exists : {dest_dir}")
    
    
    for filename in os.listdir(source_dir):
        src_file = os.path.join(source_dir,filename)
        dest_file = os.path.join(dest_dir, filename)
        if os.path.isfile(src_file):
            shutil.copy2(src_file,dest_file)
            print(f"Copied: {src_file} -> {dest_file}")

def main():
   
    copy_directory_files()

if __name__ == "__main__":
    main()
