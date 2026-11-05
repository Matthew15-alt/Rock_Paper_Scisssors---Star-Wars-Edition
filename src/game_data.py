import random

game_stats = {
    "wins": 0,
    "losses": 0,
    "ties": 0,
}


def view_stats():
    print("\nCurrent Statistics:")
    print(f"Games Won: {game_stats['wins']}")
    print(f"Games Lost: {game_stats['losses']}")
    print(f"Games Tied: {game_stats['ties']}")
    total = game_stats["wins"] + game_stats["losses"] + game_stats["ties"]
    print(f"Total Games: {total}")


def game_play():
    while True:
        player_move = (
            input("Choose a move (Rock, Paper, or Scissors): ").strip().lower()
        )
        game_moves = ["rock", "paper", "scissors"]
        computer_move = random.choice(game_moves)
        print(f"\nYou chose {player_move}, computer chose {computer_move}")

        if player_move == computer_move:
            print(f"You and the computer chose {player_move}. It's a tie!")
        elif player_move == "rock" and computer_move == "scissors":
            print("Rock beats Scissors. You Win!")
