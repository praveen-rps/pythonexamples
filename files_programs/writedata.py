def write_to_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content + '\n')

def main():
    file_name = 'user_input.txt'

    print("Enter text (type 'exit' or 'quit' to stop):")

    while True:
        user_input = input("> ")

        # Check if the user wants to exit
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting program.")
            break

        # Write input to file
        write_to_file(file_name, user_input)

    print(f"Content written to '{file_name}'.")

if __name__ == "__main__":
    main()
