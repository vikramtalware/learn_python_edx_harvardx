import sys

i = 0

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".py") == True:
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if not (line.lstrip().startswith("#") or line.lstrip() == ''):
                    i += 1
            print(i)
    except(FileNotFoundError):
        sys.exit("File does not exist")
else:
    sys.exit("Not a Python file")
