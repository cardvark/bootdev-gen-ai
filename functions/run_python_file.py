import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    abs_full_path = os.path.abspath(full_path)

    if not abs_full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(full_path):
        return f'Error: File "{file_path}" not found.'
    
    if not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        completed_process = subprocess.run(
            ["python", file_path, *args],
            capture_output=True,
            timeout=30,
            cwd=working_directory,
            text=True,
        )

        standard_output = f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"

        if completed_process.returncode != 0:
            return f"Process exited with code {completed_process.returncode}"

        if not completed_process.stdout and not completed_process.stderr:
            return "No output produced"
        
        return standard_output
        
    except Exception as e:
        print(f"Error: {e}")


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the selected python file. Returns STDOUT from the python file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the python file to be run.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items={
                    "type": "string"
                },
                description="List of arguments for the file. Arguments within the array should be in string format."
            ),
        },
    ),
)