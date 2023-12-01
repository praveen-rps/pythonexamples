import csv

def merg_csv_files(inputfile1,inputfile2,outputfile):

    # It is used to find the unique rows in the given file
    def read_csv(file):
        unique_row = set()
        with open(file,"r",newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                unique_row.add(tuple(row))
        return unique_row

    # Reqd unique rows from both the csv files
    unique_rows_file1 = read_csv(inputfile1)
    unique_rows_file2 = read_csv(inputfile2)

    # Identify the rows that are unique to inputfile2
    unique_to_file2 = unique_rows_file2 - unique_rows_file1

    #Combine both the files
    merged_rows = unique_rows_file1.union(unique_to_file2 )

    #Write to a new file
    with open(outputfile,"w",newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in merged_rows:
            writer.writerow(row)

if __name__ == "__main__":
    merg_csv_files("data.csv","data1.csv",outputfile="output.csv")
    print("unique data merged from two files ")

