import mysql.connector

def insert_data():
    try:
        con = mysql.connector.connect(user='root',password='root',host='localhost', database='fisglobal')
        cur = con.cursor();

        # read data from keyboard
        id = int(input("enter id "))
        name = input("enter name")
        dept = input("enter dept")
        sal = int(input("enter salary"))
        query = "insert into employees(id,name,dept,sal) values (%s,%s,%s,%s)"
        data = (id,name,dept,sal)
        cur.execute(query,data)
        con.commit()

        print("Data inserted into table")
        con.close()
    except:
       print("Error established")




if __name__ == "__main__":
    insert_data()










