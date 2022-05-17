LINE_WIDTH = 85


def started(msg=""):
    output = f"Operation started: {msg}..."
    dashes = "-" * LINE_WIDTH
    print(f"{dashes}\n{output}\n")


def completed():
    dashes = "-" * LINE_WIDTH
    print(f"\nOperation completed.\n{dashes}\n")


def error(msg):
    print(f"Error! {msg}\n")


def menu():
    print(f"""Please select one of the following options:
    {"[years]":<10} List unique years
    {"[tally]":<10} Tally up medals
    {"[team]":<10} Tally up medals for each team
    {"[exit]":<10} Exit the program
    """)
    selection = input("Your selection: ")
    return selection.strip().lower()


def display_medal_tally(tally):
    print(f"| {'Gold':<10} | {tally['Gold']:<10} |")
    print(f"| {'Silver':<10} | {tally['Silver']:<10} |")
    print(f"| {'Bronze':<10} | {tally['Bronze']:<10} |")


def display_team_medal_tally(team_tally):
    for team, tally in team_tally.items():
        print(team)
        print(f"\tGold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")


def display_years(years):
    sorted_years = sorted(years, reverse=True)
    for year in sorted_years:
        print(year)
