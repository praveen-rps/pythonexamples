import mysql.connector
def read_data_from_mysql():

 try:
    # Create a connection Object
    con = mysql.connector.connect(user='root',password='root',host='localhost',database='fisglobal')

    #2. create a cursor

    cur = con.cursor()


    #3. execute a Query  -- execute method
    cur.execute("select * from employees")

# [(1001,praveen,finance,5000),
    #(1002,kumar,qualty,4500),
    #
    # (),()]
    #4. fetch the values from cursor

    rows = cur.fetchall()

    #5. display all records
    for row in rows:
        print(row)

 except mysql.connector.Error as err:
     print(f"Error: {err}")


 finally:
     cur.close()
     con.close()


if __name__ == "__main__":
    read_data_from_mysql()






