import mysql.connector

def create_connection():
    con = mysql.connector.connect(user='root', password='root', host='localhost', database='fisglobal')
    print("inside connection method")
    return con