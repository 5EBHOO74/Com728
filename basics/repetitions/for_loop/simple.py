# Ask user for number of mountains
print("How many mountains should I display?")
mountains = int(input())

# Display mountains
print("Displaying...")

for mountain in range(mountains):
  print("""
           __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\

  """)
