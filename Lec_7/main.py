def main():
    while True:
        try:
            filename = input("Enter the name of the text file you want to open: ")
            if filename.isnumeric():
                raise ValueError("File name cannot be a numeric value.")
            with open(filename, "r") as file:
                content = file.read()
            print("\n--- File Content ---")
            print(content)
            break
        except FileNotFoundError:
            print("Error: The file does not exist. Please enter a valid file name.")
        except ValueError as ve:
            print(f"Error: {ve}")

    write_option = input("\nDo you want to write to this file or a new file? (Enter 'same' or 'new'): ").strip().lower()

    try:
        if write_option == "same":
            write_file = filename
        elif write_option == "new":
            write_file = input("Enter the name of the new file: ").strip()
        else:
            raise ValueError("Invalid option. Please enter 'same' or 'new'.")
        
        content_to_write = input("Enter the content you want to write to the file: ")
        with open(write_file, "w") as file:
            file.write(content_to_write)
    except FileNotFoundError:
        print("Error: Could not create or access the file. Please try again.")
    except ValueError as ve:
        print(f"Error: {ve}")
    else:
        print(f"Success: Content written to the file '{write_file}' successfully.")
    finally:
        print(f"The file '{write_file}' has been closed (if it was opened).")

if __name__ == "__main__":
    main()
