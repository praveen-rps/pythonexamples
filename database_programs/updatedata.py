import mysql.connector

def update_salary(cursor, employee_id, current_salary):
    new_salary = current_salary + 500
    cursor.execute("UPDATE employees SET salary = %s WHERE employee_id = %s", (new_salary, employee_id))

def main():
    # Modify these parameters with your MySQL connection details
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'fisglobal'
    }

    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Read employee information
        cursor.execute("SELECT employee_id, salary FROM employees")
        employees = cursor.fetchall()

        # Update salary if it is less than 500
        for employee_id, salary in employees:
            if salary < 500:
                update_salary(cursor, employee_id, salary)

        # Commit the changes to the database
        connection.commit()

        print("Salary updates successful!")

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
