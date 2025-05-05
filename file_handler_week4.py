def file_modifier():
    """
    This program:
    1. Asks user for a filename to read
    2. Handles errors if file doesn't exist or can't be read
    3. Modifies the content (in this case, converts to uppercase)
    4. Writes the modified content to a new file
    5. Handles potential write errors
    """
    
    # Get input filename from user with error handling
    while True:
        input_filename = input("Enter the name of the file to read: ")
        try:
            with open(input_filename, 'r') as file:
                content = file.read()
            break  # Exit loop if file read successfully
        except FileNotFoundError:
            print(f"Error: The file '{input_filename}' does not exist. Please try again.")
        except PermissionError:
            print(f"Error: Permission denied when trying to read '{input_filename}'. Please try another file.")
        except IOError as e:
            print(f"Error reading file: {e}. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")
    
    # Modify the content (convert to uppercase in this example)
    modified_content = content.upper()
    print("\nOriginal content:")
    print(content)
    print("\nModified content (uppercase):")
    print(modified_content)
    
    # Get output filename from user with error handling
    while True:
        output_filename = input("\nEnter the name of the file to write the modified content: ")
        try:
            with open(output_filename, 'w') as file:
                file.write(modified_content)
            print(f"\nSuccess! Modified content written to '{output_filename}'")
            break  # Exit loop if file written successfully
        except PermissionError:
            print(f"Error: Permission denied when trying to write to '{output_filename}'. Please try another filename.")
        except IOError as e:
            print(f"Error writing file: {e}. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

if __name__ == "__main__":
    print("File Read & Write Challenge with Error Handling\n")
    file_modifier()
