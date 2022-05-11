bad_file_path = "bad_file"

try:
    with open(bad_file_path) as file:
        print(file.readlines())
except IOError:
    print("Cannot read file.")