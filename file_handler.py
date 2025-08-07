def find_and_replace(file_path, word_to_find, word_to_replace):
    try:
        # Read content from file
        with open(file_path, 'r') as file:
            content = file.read()

        # Replace the word
        modified_content = content.replace(word_to_find, word_to_replace)

        # Save modified content back to file
        with open(file_path, 'w') as file:
            file.write(modified_content)

        print(f"Successfully replaced '{word_to_find}' with '{word_to_replace}'.")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print("Error: Permission denied while accessing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("=== File Find and Replace Tool ===")
    file_path = input("Enter file path: ")
    word_to_find = input("Word to find: ")
    word_to_replace = input("Word to replace with: ")

    find_and_replace(file_path, word_to_find, word_to_replace)
