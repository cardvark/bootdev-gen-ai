import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.call_function import available_functions, call_function

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    content_request = sys.argv
    verbose = "--verbose" in sys.argv

    if len(content_request) < 2:
        print("No prompt provided.")
        sys.exit(1)

    messages = [
        types.Content(role="user", parts=[types.Part(text=content_request[1])]),
    ]

    if verbose:
        print(f"User prompt: {content_request[1]}")

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):   
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt),
        )

    print(response.text)
    
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if not response.function_calls:
        return response.text

    for call in response.function_calls:
        # print(f"Calling function: {call.name}({call.args})")
        function_call_result = call_function(call, verbose)

        if not function_call_result.parts[0].function_response.response:
            raise Exception("No response to function call")
    
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
            


if __name__ == "__main__":
    main()
