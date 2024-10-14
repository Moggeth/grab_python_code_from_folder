import os
import pyperclip

def collect_python_scripts_text(input_directory):
    output_text = ""
    
    for root, _, files in os.walk(input_directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        script_content = f.read()
                    # Format the content as specified
                    rel_path = os.path.relpath(file_path, input_directory)
                    output_text += f"{rel_path}\n```python\n{script_content}\n```\n\n"
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    
    return output_text

def copy_to_clipboard(text):
    try:
        pyperclip.copy(text)
    except pyperclip.PyperclipException as e:
        print("Error copying to clipboard. Make sure clipboard functionality is available.")
        raise e

def main():
    try:
        # Get the input directory from clipboard
        input_directory = pyperclip.paste().strip()
        
        # Check if the directory exists
        if not os.path.isdir(input_directory):
            raise ValueError("The directory path from the clipboard does not exist. Please copy a valid directory path.")
        
        # Collect all Python scripts text
        all_scripts_text = collect_python_scripts_text(input_directory)
        
        # Copy the result to the clipboard
        copy_to_clipboard(all_scripts_text)
        print("All scripts text has been copied to the clipboard.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Ensure pyperclip is available and then run the main function
if __name__ == "__main__":
    try:
        import pyperclip
    except ImportError:
        print("Please install the pyperclip module by running 'pip install pyperclip'")
    else:
        main()
