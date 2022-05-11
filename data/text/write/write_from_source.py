source_file_path = input("Enter source file path: ") or "quotes.txt"
destination_file_path = input("Enter destination file path: ") or "output.txt"
lines = []

try:
    with open(source_file_path) as source_file:
        for line in source_file:
            lines.append(line.strip())
        print("The data has been loaded.")

    with open(destination_file_path, 'w') as destination_file:
        for line in lines:
            destination_file.write(f"{line}\n")
        print("The data has been written.")
except IOError:
    print("Cannot write to the file.")