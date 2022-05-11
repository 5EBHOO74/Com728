file_path = "sample.csv"

try:
  with open(file_path, 'w') as file:
    file.write("Sample Song,Sample Artist,Sample Category,Sample Year")
except IOError:
    print("Cannot read file.")