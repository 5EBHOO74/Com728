def display_ladder(steps):
    # Display each step
    for step in range(steps):
        print("| |")
        print("***")

    # Display bottom of ladder
    print("| |")

def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)

create_ladder()