import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    # print(full_path)
    abs_full_path = os.path.abspath(full_path)
    # print(abs_full_path)

    if not abs_full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(full_path):
        # print(full_path)
        return f'Error: "{directory}" is not a directory'
    
    try: 
        files_info = []
        for item in os.listdir(full_path):
            # print(f"Parsing {item}")
            pathed_item = os.path.join(full_path, item)
            size = os.path.getsize(pathed_item)
            files_info.append(f"- {item}: file_size={size} bytes, is_dir={os.path.isdir(pathed_item)}")
        return "\n".join(files_info)
    except Exception as e:
        print(f"Error: {e}")


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)