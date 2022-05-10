# Ask user for eye character
print("Please enter an eye character:")
eye = input()

# Ask user for the length of the glasses
print("Please enter the length of the glasses:")
length = int(input())


print(f"#########{' ' * length}#########")
print(f"#   {eye}   {'#' * (length + 2)}   {eye}   #")
print(f"#########{' ' * length}#########")

print()