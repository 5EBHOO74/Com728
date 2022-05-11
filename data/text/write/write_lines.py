file_path = input("Enter a file path: ") or "output.txt"
lines = ["This is the first line.\n", "This is the second line.\n", "This is the third line.\n"]
try:
    with open(file_path, 'w') as file:
        file.writelines(lines)
        print("The data has been written to the file.")
except IOError:
    print("Cannot write to the file.")