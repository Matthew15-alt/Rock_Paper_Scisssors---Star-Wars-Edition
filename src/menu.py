from game_data import game_stats
from game_data import view_stats
from game_data import game_play
from game_data import view_scoreboard


def show_menu(player_name):
    is_running = True

    while is_running:
        print("\nMenu:")
        print("1. Play Round")
        print("2. View Stats")
        print("3. View Scoreboard")
        print("4. Exit")

        choice = input("Choose an option (Enter 1-4): ").strip()

        if choice == "1":
            game_play(player_name)
        elif choice == "2":
            view_stats(player_name)
        elif choice == "3":
            view_scoreboard()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")
