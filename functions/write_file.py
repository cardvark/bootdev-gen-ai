import os
from google.genai import types

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    abs_full_path = os.path.abspath(full_path)

    if not abs_full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, "w") as file:
            file.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        print(f"Error: {e}")


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to the selected file, replacing all contents if any exist. Returns confirmation of execution, along with number of characters written.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to be written.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to be written in the selected file."
            ),
        },
    ),
)