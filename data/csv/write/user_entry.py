file_path = "user_entries.csv"

try:
  with open(file_path, 'w') as file:
    for count in range(3):
      # write out the headings
      file.write("year,artist,song title")

      # write out the user's songs
      year = int(input("Please enter year: "))
      artist = input("Please enter artist: ")
      title = input("Please enter song title: ")
      file.write(f"\n{year},{artist},{title}")
except IOError:
    print("Cannot read file.")
