import csv
import mysql.connector

def create_connection():
    con = mysql.connector.connect(user='root', password='root', host='localhost', database='fisglobal')
    print("inside connection method")
    return con

def fetch_data():
    con = create_connection()
    cursor = con.cursor(dictionary=True)
    query = "select * from emp"
    cursor.execute(query)
    data = cursor.fetchall()
    print("Before processing...")
    for row in data:
        print(row)
    return data

def update_data(data):
    updated_data = []
    for row in data:
        if row['sal'] <= 45000:
            row['sal'] += 5000
        updated_data.append(row)
    return updated_data


def write_to_csv(data):
    try:
        with open("updatedcsvdata3.csv","w",newline='') as csv_file:
            fieldname = ['id','name','dept','sal']
            writer = csv.DictWriter(csv_file,fieldnames=fieldname)
            writer.writeheader()
            writer.writerows(data)
            print("Data is written to file")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    data = fetch_data()
    temp = update_data(data)
    write_to_csv(temp)



