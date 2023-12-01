import csv


def write_to_csv(file_name, data):
    try:
        with open(file_name, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
        print(f"Data written to '{file_name}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    csv_file_name = 'output.csv'
    data_to_write = []

    print("Enter data for the CSV file. Type 'exit' to stop.")
    while True:
        name = input("Enter name: ")

        # Check if the user wants to exit
        if name.lower() == 'exit':
            break

        age = input("Enter age: ")
        city = input("Enter city: ")

        data_to_write.append([name, age, city])

    write_to_csv(csv_file_name, data_to_write)


if __name__ == "__main__":
    main()
