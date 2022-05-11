file_path = input("Enter a file path: ") or "output.txt"

try:
    with open(file_path, 'w') as file:
        file.write("data has been overwritten!")
        print("The data has been written to the file.")
except IOError:
    print("Cannot write to the file.")