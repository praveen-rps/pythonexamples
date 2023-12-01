import csv
import mysql.connector

# Function to connect to MySQL and fetch data
def fetch_data():
    # Update the following with your MySQL connection details
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='fisglobal'
    )

    cursor = connection.cursor(dictionary=True)

    # Query to fetch data from the emp table
    query = 'SELECT * FROM emp'

    cursor.execute(query)

    # Fetch data
    data = cursor.fetchall()

    # Close the connection
    cursor.close()
    connection.close()

    return data

# Function to update and write data to CSV
def update_and_write_csv(data):
    # Check if the salary is less than 500 and increment by 100
    try:
        updated_data = []
        for row in data:
            if row['sal'] <= 45000:
                row['sal'] += 5000
            updated_data.append(row)

    # Write the updated data to a CSV file
        with open('e://data/updated_emp_data.csv', 'w', newline = '') as csv_file:
            fieldnames = ['empid', 'name', 'dept', 'sal']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write the header
            writer.writeheader()

            # Write the data
            writer.writerows(updated_data)

        print("Updated data written to 'updated_emp_data.csv'.")
    except Exception as e:
        print(e)

# Main program
if __name__ == "__main__":
    # Fetch data from the MySQL database
    emp_data = fetch_data()

    # Display the original data
    print("Original Data:")
    print(emp_data)

    # Update and write to CSV
    update_and_write_csv(emp_data)
    print("Data written to csv file")