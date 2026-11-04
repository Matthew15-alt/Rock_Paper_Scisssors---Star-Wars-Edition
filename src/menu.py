from game_data import game_stats

print(game_stats)


def show_menu():
    is_running = True
    while is_running:
        print("\nMenu:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")
        break

    choice = input("Choose an option: ").strip()

    if choice == "1":
        print("You chose: Rock")
    elif choice == "2":
        print("You chose: Paper")
    elif choice == "3":
        print("You chose: Scissors")
    elif choice == "4":
        is_running = False
    else:
        print("Invalid choice. Please try again.")
