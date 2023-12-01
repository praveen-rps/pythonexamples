import mysql.connector
from database_programs.dbutils import *
import csv

def read_csv(file_name):
    data = []
    try:
        with open(file_name, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                #data.append(row)
                print(row[0])
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data

def readDataFromCsv():
    try:
        with open("data.csv","r") as file:
            content = file.read();
            print(content)
    except:
        print("Could not able to read file")

if __name__ == "__main__":
    #readDataFromCsv()
    read_csv('data.csv')

