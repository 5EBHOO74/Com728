try:
    file_path = input("Enter a file path: ")
    with open(file_path) as file:
        print(file.readlines())
except IOError:
    print("Cannot read file.")