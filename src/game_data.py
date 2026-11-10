import json
import os
import random

SCOREBOARD_FILE = "scoreboard.json"


def load_scoreboard():
    if not os.path.exists(SCOREBOARD_FILE):
        return {}

    with open(SCOREBOARD_FILE, "r") as file:
        return json.load(file)


def save_scoreboard(game_stats):
    with open(SCOREBOARD_FILE, "w") as file:
        json.dump(game_stats, file, indent=4)


game_stats = load_scoreboard()


def add_player(player_name):
    if player_name not in game_stats:
        game_stats[player_name] = {
            "wins": 0,
            "losses": 0,
            "ties": 0,
        }

        save_scoreboard(game_stats)


def get_total_games(stats):
    return stats["wins"] + stats["losses"] + stats["ties"]


def get_win_rate(stats):
    total_games = get_total_games(stats)

    if total_games == 0:
        return 0

    return round((stats["wins"] / total_games) * 100)


def view_stats(player_name):
    stats = game_stats[player_name]

    total_games = get_total_games(stats)
    win_rate = get_win_rate(stats)

    print(f"\nStats for {player_name}:")
    print(f"Wins: {stats['wins']}")
    print(f"Losses: {stats['losses']}")
    print(f"Ties: {stats['ties']}")
    print(f"Total Games: {total_games}")
    print(f"Win Rate: {win_rate:.0f}%")


def game_play(player_name):
    while True:
        player_move = (
            input("Choose a faction (Jedi, Sith, or Clone Trooper): ").strip().lower()
        )
        game_moves = ["jedi", "sith", "clone trooper"]
        computer_move = random.choice(game_moves)
        print(f"\nYou chose {player_move}, computer chose {computer_move}")

        if player_move == computer_move:
            print("It's a tie!")
            game_stats[player_name]["ties"] += 1
            save_scoreboard(game_stats)
        elif player_move == "jedi" and computer_move == "sith":
            print("Jedi defeats Sith through discipline and the Light Side. You win!")
            game_stats[player_name]["wins"] += 1
            save_scoreboard(game_stats)
        elif player_move == "jedi" and computer_move == "clone trooper":
            print("Order 66 catches the Jedi by surprise. You lose!")
            game_stats[player_name]["losses"] += 1
            save_scoreboard(game_stats)
        elif player_move == "sith" and computer_move == "jedi":
            print("Jedi defeats Sith through discipline and the Light Side. You lose!")
            game_stats[player_name]["losses"] += 1
            save_scoreboard(game_stats)
        elif player_move == "sith" and computer_move == "clone trooper":
            print("Sith manipulate and command armies of clones. You win!")
            game_stats[player_name]["wins"] += 1
            save_scoreboard(game_stats)
        elif player_move == "clone trooper" and computer_move == "jedi":
            print("Order 66 catches the Jedi by surprise. You win!")
            game_stats[player_name]["wins"] += 1
            save_scoreboard(game_stats)
        elif player_move == "clone trooper" and computer_move == "sith":
            print("Sith manipulate and command armies of clones. You lose!")
            game_stats[player_name]["losses"] += 1
            save_scoreboard(game_stats)
        else:
            print("Not a game move! Please input valid game move.")

        play_again = input("Would you like to play again? (y/n): ")
        if play_again.strip().lower() != "y":
            break


def view_scoreboard():
    print("\n=== SCOREBOARD ===")

    if not game_stats:
        print("No players found.")
        return

    for player, stats in game_stats.items():
        total_games = get_total_games(stats)
        win_rate = get_win_rate(stats)

        print(f"\nPlayer: {player}")
        print(f"Wins: {stats['wins']}")
        print(f"Losses: {stats['losses']}")
        print(f"Ties: {stats['ties']}")
        print(f"Total Games: {total_games}")
        print(f"Win Rate: {win_rate}")
