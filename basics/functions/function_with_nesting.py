# The function
def identify():
    # Ask user for what lies ahead
    print("What lies before us?")
    response = input()

    # Display message
    if response == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")


# Call to function
identify()