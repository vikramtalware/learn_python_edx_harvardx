import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv"):
        try:
            print(ascii_art(sys.argv[1]))
        except(FileNotFoundError):
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV File")

def ascii_art(filename):
    with open(filename) as file:
        reader = csv.reader(file)
        table = tabulate(reader, headers = "firstrow", tablefmt = "grid")
        return table

if __name__ == "__main__":
    main()
