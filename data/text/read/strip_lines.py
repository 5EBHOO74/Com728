file_path = input("Enter a file path: ") or "quotes.txt"
try:
    with open(file_path) as file:
        for line in file.readlines():
            print(line.strip())
except IOError:
    print("Cannot read file.")