
def write_to_file(filename,content):
    with open(filename,"a") as file:
        file.write(content+ '\n')


def main():
    filename = "e://data/user_input.txt"
    print("enter the text - type exit or quit to stop")
    while True:
        data = input();
        if data.lower() in ['exit', 'quit']:
            break;
        else:
            write_to_file(filename,data)

if __name__ == "__main__":
    main()