# Start your CLI app here.
#
# Run it with:  python3 src/main.py
#
# The brief is in PROJECT.md.
from game_data import add_player
from menu import show_menu


def start_app():
    player_name = input("Please type in your name: ").strip()
    add_player(player_name)
    print(
        f"Hello {player_name}, welcome to my Rock-Paper-Scissors game, Star Wars Edition!"
    )
    show_menu(player_name)
    print("\nThanks for playing!")


if __name__ == "__main__":
    start_app()
