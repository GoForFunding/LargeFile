import re

def replace_body_content(file_path, user_body_code):
    """
    Replaces the current <body> tag and its contents in the HTML file with the user-provided body code.

    Parameters:
        file_path (str): The path to the HTML file (e.g., "index.html").
        user_body_code (str): The new <body> code provided by the user.
    """
    try:
        # Read the current content of the HTML file
        with open(file_path, 'r') as file:
            html_content = file.read()
        
        # Ensure the user-provided code includes the <body> tag
        if not re.search(r"<body[^>]*>.*?</body>", user_body_code, re.DOTALL):
            raise ValueError("The provided body code must include a valid <body> tag.")

        # Replace the existing <body> tag and its content with the user-provided code
        updated_content = re.sub(
            r"<body[^>]*>.*?</body>",  # Regex to match the current <body> tag and its content
            user_body_code,  # Replace with user-provided body code
            html_content,
            count=1,  # Replace only the first occurrence
            flags=re.DOTALL  # Allow multiline matches
        )
        
        # Write the updated content back to the HTML file
        with open(file_path, 'w') as file:
            file.write(updated_content)
        
        print("The <body> content has been successfully replaced.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
