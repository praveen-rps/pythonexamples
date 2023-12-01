import csv

def read_csv(csvfile):
    data = []
    try:
        with open(csvfile,'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
            for line in data:
                print(line)

    except:
        print("File error")


if __name__ == "__main__":
    read_csv('data.csv')

