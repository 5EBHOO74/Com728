# Ask user for numbers
print("Please enter the first whole number?")
first_number = int(input())

print("Please enter the second whole number?")
second_number = int(input())

print("Please enter the third whole number?")
third_number = int(input())

even_numbers = 0
odd_numbers = 0

# Determine which numbers are even and which are odd
if first_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if second_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if third_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

# Display result
print(f"There were {even_numbers} even and {odd_numbers} odd numbers.")