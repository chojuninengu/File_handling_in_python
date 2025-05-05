def modify_content(content):
    """Example modification function - you can customize this"""
    # Convert to uppercase as a simple modification
    return content.upper()

def file_operations():
    print("File Read & Write Program")
    print("-------------------------")
    
    while True:
        try:
            # Ask user for input filename
            input_filename = input("Enter the name of the file to read: ").strip()
            
            # Read the file
            with open(input_filename, 'r') as file:
                original_content = file.read()
            
            # Modify the content
            modified_content = modify_content(original_content)
            
            # Ask user for output filename
            output_filename = input("Enter the name of the new file to create: ").strip()
            
            # Write the modified content to new file
            with open(output_filename, 'w') as file:
                file.write(modified_content)
            
            print(f"\nSuccess! Modified content written to {output_filename}")
            break
            
        except FileNotFoundError:
            print(f"Error: The file '{input_filename}' was not found. Please try again.")
        except PermissionError:
            print(f"Error: You don't have permission to read '{input_filename}' or write to '{output_filename}'.")
        except IsADirectoryError:
            print(f"Error: '{input_filename}' is a directory, not a file.")
        except UnicodeDecodeError:
            print(f"Error: Could not decode the file '{input_filename}'. It might be a binary file.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
        
        # Ask if user wants to try again
        choice = input("\nWould you like to try again? (yes/no): ").lower()
        if choice != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    file_operations()
