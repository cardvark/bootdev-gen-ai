import os
from functions.config import *

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    abs_full_path = os.path.abspath(full_path)

    print(full_path)

    if not abs_full_path.startswith(os.path.abspath(working_directory)):
        return f"Error: Cannot read '{file_path}' as it is outside the permitted working directory"
        
    if not os.path.isfile(full_path):
        return f"Error: File not found or is not a regular file:'{file_path}'"

    try:
        with open (full_path, 'r') as file:
            file_content = file.read(FILE_LENGTH_LIMIT)
            # print(file_content)
            if len(file_content) == FILE_LENGTH_LIMIT:
                print(f"[...File '{file_path}' truncated at {FILE_LENGTH_LIMIT} characters]")
    except Exception as e:
        print(f"Error: {e}")
        
    
    return file_content