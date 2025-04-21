import os
import shutil

def copy_static(source_dir, dest_dir):
    # Clear destination directory if it exists
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    
    # Create fresh destination directory
    os.mkdir(dest_dir)
    
    # Now recursively copy everything
    copy_source_dir_to_dest(source_dir, dest_dir)


def copy_source_dir_to_dest(source,dest): # path to static dir --> dest: public
    # List everything in the source directory
    for item in os.listdir(source):
        # Create full paths
        source_path = os.path.join(source, item)
        dest_path = os.path.join(dest, item)
        
        # Handle files vs directories
        if os.path.isfile(source_path):
          print(f"Copying file: {source_path} to {dest_path}")
          shutil.copy(source_path, dest_path)
            
        else:
            # Create the destination directory before copying into it
            os.mkdir(dest_path)
            print(f"Created directory: {dest_path}")
            copy_source_dir_to_dest(source_path,dest_path)
            