import os
import shutil

def collect_sets(source_dir='sets', output_dir='all_sets_unified'):
    """
    Iterates over the folders in source_dir in alphabetical order and 
    copies files to output_dir with the name format <set_name>_<image_name>.<ext>.
    """
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    # Get sorted list of set folders
    set_folders = sorted([f for f in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, f))])

    count = 0
    for set_name in set_folders:
        set_path = os.path.join(source_dir, set_name)
        
        # Get sorted list of files in the set folder
        files = sorted([f for f in os.listdir(set_path) if os.path.isfile(os.path.join(set_path, f))])
        
        for file_name in files:
            # Skip hidden files
            if file_name.startswith('.'):
                continue
                
            src_file_path = os.path.join(set_path, file_name)
            
            # Construct the new filename: <set_name>_<image_name>
            new_file_name = f"{set_name}_{file_name}"
            dst_file_path = os.path.join(output_dir, new_file_name)
            
            # Copy the file
            try:
                shutil.copy2(src_file_path, dst_file_path)
                count += 1
            except Exception as e:
                print(f"Error copying {file_name} from {set_name}: {e}")

    print(f"Done! Copied {count} files to '{output_dir}'.")

if __name__ == "__main__":
    # Adjust paths if necessary
    collect_sets()
