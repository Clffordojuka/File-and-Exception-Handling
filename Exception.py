def modify_content(content):
    """
    Modify the content of the file.
    Example: Convert text to uppercase.
    """
    return content.upper()  # Customize this function for other modifications.

def read_and_write_files():
    try:
        # User inputs an existing filename
        input_file = input("Enter the name of the file to read: ")
        
        # Open and read the input file
        with open(input_file, "r") as file:
            content = file.read()
        
        # Modify the content
        modified_content = modify_content(content)
        
        # Ask for the output filename
        output_file = input("Enter the name of the file to write the modified content: ")
        
        # Write the modified content to the new file
        with open(output_file, "w") as file:
            file.write(modified_content)
        
        print(f"Modified content written to {output_file} successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read/write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    read_and_write_files()
