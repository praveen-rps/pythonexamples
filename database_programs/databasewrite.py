import mysql.connector

def insert_data():
    # Replace these variables with your actual MySQL connection information
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_HOST = 'localhost'
    MYSQL_DATABASE = 'fisglobal'

    try:
        # Create a MySQL connection
        connection = mysql.connector.connect(
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            host=MYSQL_HOST,
            database=MYSQL_DATABASE
        )

        # Create a cursor to execute queries
        cursor = connection.cursor()

        # Get input from the user
        id_val = input("Enter ID: ")
        name_val = input("Enter Name: ")
        dept_val = input("Enter Department: ")
        sal_val = input("Enter Salary: ")

        # Insert the data into the database
        query = "INSERT INTO employees (id, name, dept, sal) VALUES (%s, %s, %s, %s);"
        data = (id_val, name_val, dept_val, sal_val)
        cursor.execute(query, data)

        # Commit the transaction
        connection.commit()

        print("Data inserted successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()

        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    insert_data()
