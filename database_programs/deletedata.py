
from dbutils import *

def delete_data(conn):

    try:
       cur = conn.cursor()
       if cur is not None:
           print("Connection established")
       else:
           print("connection not established")

       query = '''delete from employees where id=%s '''

       eid = int(input("enter employee id"))

       cur.execute(query,[eid])

       print("deleted")

       conn.commit()
       #print("record deleted")

    except:
        print("Error occur")

if __name__ == "__main__":
    delete_data(create_connection())