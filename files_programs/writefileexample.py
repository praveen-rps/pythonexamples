def write_data(filename):
    try:
        file = open(filename,"a")
        file.write("this will be appended to previous data"+ '\n')
        print("data written")
    except:
        print("File write is aborted")
    finally:
        file.close()


if __name__ == "__main__":
    write_data("e://data/output.txt")