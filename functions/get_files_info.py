import os
import sys

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    # print(full_path)
    abs_full_path = os.path.abspath(full_path)
    # print(abs_full_path)
    cwd_path = os.getcwd()



    if not abs_full_path.startswith(os.path.abspath(working_directory)):
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        # sys.exit()
        return
    
    if not os.path.isdir(full_path):
        # print(full_path)
        print(f'Error: "{directory}" is not a directory')
        # sys.exit()
        return
    
    try: 
        for item in os.listdir(full_path):
            # print(f"Parsing {item}")
            pathed_item = os.path.join(full_path, item)
            size = os.path.getsize(pathed_item)
            print(f"- {item}: file_size={size} bytes, is_dir={os.path.isdir(pathed_item)}")
    except Exception as e:
        print(f"Error: {e}")