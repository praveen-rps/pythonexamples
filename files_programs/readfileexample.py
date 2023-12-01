
def display_contents(filename):
    try:
        file = open(filename,"r")
        data = file.readlines()

        for d in data:
            print(d.upper())

        print(d)

    except FileNotFoundError:
        print("File is not found to read")

    finally:
        file.close()


if __name__ == "__main__":
    display_contents("e://data/input.txt")

