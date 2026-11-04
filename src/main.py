# Start your CLI app here.
#
# Run it with:  python3 src/main.py
#
# The brief is in PROJECT.md.
from menu import show_menu


def start_app():
    print("Welcome to my Rock-Paper-Scissors Game!")
    show_menu()
    print("\nGoodbye!")


if __name__ == "__main__":
    start_app()
