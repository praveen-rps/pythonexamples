import csv

data_to_write = [
    ['empid','name','dept'],
    [10001,'praveen','finance'],
    [10002,'kumar','quality'],
    [10003,'satish','operations']
]

csv_file='e://data/testoutput.csv'


def write_csv(csv_file,data_to_write):
    try:
        with open(csv_file,"w",newline='') as file:
            writer = csv.writer(file)
            for row in data_to_write:
                writer.writerow(row)
        print("Data written to csv file")
    except:
        print("Error in file")

    finally:
        file.close()

if __name__ == "__main__":
    write_csv(csv_file,data_to_write)

