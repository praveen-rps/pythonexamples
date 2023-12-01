import mysql.connector

def read_and_display_data():
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

        # Execute a simple SELECT query
        query = "SELECT * FROM employees;"
        cursor.execute(query)

        # Fetch all the rows from the result set
        rows = cursor.fetchall()

        # Display the data on the console
        for row in rows:
            print(row)

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
    read_and_display_data()
