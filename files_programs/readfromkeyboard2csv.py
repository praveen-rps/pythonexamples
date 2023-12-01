import csv

def write_csv(data_to_write):
    try:
        with open('e://data/testoutput1.csv','w',newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data_to_write)
        print("Data written to csv file")
    except Exception as e:
        print(e)

    #finally:
        #file.close()

def readData():
    data = []
    print("Enter contents type exit or quit to stop")
    while True:
        name = input("enter name")
        if name.lower() == "exit":
            break;
        empid = input("enter employee id")
        dept = input("enter dept")
        data.append([empid,name,dept])
    return data


if __name__ == "__main__":
    write_csv(readData())

