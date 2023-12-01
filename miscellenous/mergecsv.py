import csv

def merge_csv_files(file1_path, file2_path, output_file_path):
    # Function to read CSV file and return a set of unique rows
    def read_csv(file_path):
        unique_rows = set()
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                unique_rows.add(tuple(row))
        return unique_rows

    # Read unique rows from both CSV files
    unique_rows_file1 = read_csv(file1_path)
    unique_rows_file2 = read_csv(file2_path)

    # Identify rows that are unique to file2
    unique_to_file2 = unique_rows_file2 - unique_rows_file1

    # Combine unique rows from both files
    merged_rows = unique_rows_file1.union(unique_to_file2)

    # Write the merged rows to a new CSV file
    with open(output_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in merged_rows:
            writer.writerow(row)

    print(f'Merged CSV file saved to {output_file_path}')

# Replace 'file1.csv', 'file2.csv', and 'output_merged.csv' with the actual paths
file1_path = 'data.csv'
file2_path = 'data1.csv'
output_file_path = 'output_merged.csv'

merge_csv_files(file1_path, file2_path, output_file_path)

print("Data merged")
