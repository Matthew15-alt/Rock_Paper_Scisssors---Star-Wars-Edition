from game_data import game_stats
from game_data import view_stats
from game_data import game_play


def show_menu():
    is_running = True
    while is_running:
        print("\nMenu:")
        print("1. Play Round")
        print("2. View Stats")
        print("3. Exit")
        break

    choice = input("Choose an option (Enter 1-3): ").strip()

    if choice == "1":
        game_play()
    elif choice == "2":
        view_stats()
    elif choice == "3":
        is_running = False
    else:
        print("Invalid option. Please try again.")
