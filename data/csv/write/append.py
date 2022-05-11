file_path = "sample.csv"

try:
  with open(file_path, 'a') as file:
    file.write("\nMy Song,Uknown Artist,pop,2021")
except IOError:
    print("Cannot read file.")