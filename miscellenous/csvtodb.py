import csv
import mysql.connector


def create_connection():
    con = mysql.connector.connect(user='root', password='root', host='localhost', database='fisglobal')
    print("inside connection method")
    return con

# create a table in mysql database
def create_table(cursor):
    query = "create table emp(id int, name varchar(30), dept varchar(30), sal int)"
    cursor.execute(query)
    print("Table created...")

def insert_into_db(cursor,data):
    query= "insert into emp(id,name,dept,sal) values (%s,%s,%s,%s)"
    cursor.executemany(query,data)
    print("Data inserted into table")

def main():
    try:
        con = create_connection()
        cursor = con.cursor()
        # read the data from csv file

        with open('data.csv','r') as file:
            csvfile = csv.reader(file)
            next(csvfile)
            data = [tuple(row) for row in csvfile]
        print("Data is read from file")
        create_table(cursor)
        insert_into_db(cursor, data)
        con.commit()
        print("Data is successfully read from file and updated in table")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()


