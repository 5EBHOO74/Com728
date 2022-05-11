import csv

src_file_path = "../songs.csv"
dest_file_path = "output.csv"

try:
  with open(src_file_path) as src_file:
    with open(dest_file_path, 'w') as dest_file:
      csv_reader = csv.reader(src_file)
      headings = next(csv_reader)
      dest_file.write(headings)

      for values in csv_reader:
        print(f"\n{values[3]},{values[2]},{values[1]},{values[0]}")
except IOError:
    print("Cannot read file.")