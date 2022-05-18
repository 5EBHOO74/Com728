import database


def main_menu():
    print("""
    Please select one of the following options:

    [1] Display presenters
    [2] Display events
    [3] Display presenters for event
    [4] Display events for presenter
    """)

    selection = input("Your selection: ")
    return selection


def run():
    selection = main_menu()

    if selection == 1:
        print("A list of all presenters is as follows:")
        database.display_presenters()
    elif selection == 2:
        print("A list of all events is as follows:")
        database.display_events()
    elif selection == 3:
        print("Please enter the id for the event:")
        event_id = int(input())
        database.display_presenters_for_event(event_id)
    elif selection == 4:
        print("Please enter the id for the presenter:")
        presenter_id = int(input())
        database.display_events_for_presenter(presenter_id)


if __name__ == "__main__":
    run()