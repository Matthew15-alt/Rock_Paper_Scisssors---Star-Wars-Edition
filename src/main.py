# Start your CLI app here.
#
# Run it with:  python3 src/main.py
#
# The brief is in PROJECT.md.
from menu import show_menu


def start_app():
    player_name = input("Please type in your name: ").strip()
    print(f"Hello {player_name}, welcome to the Rock-Paper-Scissors Game!")
    show_menu()
    print("\nThanks for playing!")


if __name__ == "__main__":
    start_app()
