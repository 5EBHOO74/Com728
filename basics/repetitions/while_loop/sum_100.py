# Display start message
print("Calculating the sum of the first 100 numbers...")

# Declare a control variable
number = 1

# Calculate sum of first 100 numbers
total = 0

while number <= 100:
    total = total + number
    number = number + 1

# Display result
print(f"...Done! The answer is {total}")