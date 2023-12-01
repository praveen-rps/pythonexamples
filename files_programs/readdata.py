def display_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Contents of '{file_name}':\n")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_name = 'user_input.txt'  # Replace with your file name

    display_file_content(file_name)

if __name__ == "__main__":
    main()
