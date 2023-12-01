import csv
import mysql.connector

def create_table(cursor):
    # Modify the SQL query to create your table with the appropriate columns and data types
    create_table_query = """
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            salary INT
        )
    """
    cursor.execute(create_table_query)

def insert_into_db(cursor, data):
    # Modify the SQL query to match the columns in your table
    insert_query = "INSERT INTO employees (name, salary) VALUES (%s, %s)"
    cursor.executemany(insert_query, data)

def main():
    # Modify these parameters with your MySQL connection details
    db_config = {
        'host': 'your_mysql_host',
        'user': 'your_mysql_user',
        'password': 'your_mysql_password',
        'database': 'your_database_name'
    }

    # Modify this with the path to your CSV file
    csv_file_path = 'path/to/your/file.csv'

    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Create the table if it doesn't exist
        #create_table(cursor)

        # Read data from the CSV file
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip the header if exists
            data = [tuple(row) for row in csv_reader]

        # Insert data into the database
        insert_into_db(cursor, data)

        # Commit the changes to the database
        connection.commit()

        print("Data inserted into the database successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    main()
