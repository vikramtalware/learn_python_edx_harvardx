import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        clean(sys.argv[1], sys.argv[2])

def clean(input, output):
    if input.endswith(".csv") and output.endswith(".csv"):
        try:
            with open(input) as file1:
                reader = csv.DictReader(file1)
                with open(output, "w") as file2:
                    fieldnames = ["first","last","house"]
                    writer = csv.DictWriter(file2, fieldnames = fieldnames)
                    writer.writeheader()
                    for data in reader:
                        first = data["name"].split(",")[1].strip()
                        last = data["name"].split(",")[0]
                        house = data["house"]
                        writer.writerow({"first": first, "last": last, "house": house})
        except(FileNotFoundError):
            sys.exit(f"Could not read {input}")

if __name__ == "__main__":
    main()
