def read_file():
    try:
        file_name = input("Enter the file name to read: ")

        with open(file_name,"r") as file:
            content = file.read()

            print("File Content: ")
            print(content)
    except FileExistsError:
       
        print("Error: You do not have permission to access this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_file()