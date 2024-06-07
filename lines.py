import sys

lst = []

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    try:
        with open(f"{sys.argv[1]}") as file:
            for line in file:
                if not line.isspace() and not line.strip().startswith("#"):
                    lst.append(line)
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        print(len(lst))

