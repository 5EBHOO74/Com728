file_path = input("Enter a file path: ") or "output.txt"
lines = ["This is some text.", "This is some more text."]
try:
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(f"{line}\n")
        print("The data has been written to the file.")
except IOError:
    print("Cannot write to the file.")