import os

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    abs_full_path = os.path.abspath(full_path)

    if not abs_full_path.startswith(os.path.abspath(working_directory)):
        print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        return
    
    try:
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, "w") as file:
            file.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        print(f"Error: {e}")