import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 22, 35, 28],
    'Salary': [50000, 60000, 55000, 75000, 45000],
    'Department': ['HR', 'IT', 'Marketing', 'Finance', 'IT']
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Selecting specific columns
selected_columns = df[['Name', 'Age']]
print("\nSelected Columns:")
print(selected_columns)

# Selecting rows based on a condition
young_employees = df[df['Age'] < 30]
print("\nYoung Employees:")
print(young_employees)

# Selecting rows and specific columns based on a condition
it_department_salaries = df.loc[df['Department'] == 'IT', ['Name', 'Salary']]
print("\nIT Department Salaries:")
print(it_department_salaries)

# Selecting specific rows by index
specific_rows = df.loc[[0, 2, 4]]
print("\nSpecific Rows:")
print(specific_rows)

# Selecting using iloc (index-based selection)
first_two_rows = df.iloc[:2]
print("\nFirst Two Rows using iloc:")
print(first_two_rows)

# Selecting a scalar value
cell_value = df.at[1, 'Salary']
print(f"\nSalary of the employee at row 1: {cell_value}")

# Selecting using query method
high_salary_employees = df.query('Salary > 60000')
print("\nHigh Salary Employees:")
print(high_salary_employees)