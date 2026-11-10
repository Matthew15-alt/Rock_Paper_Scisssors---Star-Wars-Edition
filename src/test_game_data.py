from game_data import add_player, game_stats
from game_data import get_total_games
from game_data import get_win_rate


def test_add_player():
    game_stats.clear()

    add_player("Matthew")

    assert "Matthew" in game_stats


def test_new_player_starts_with_zero_wins():
    game_stats.clear()

    add_player("Matthew")

    assert game_stats["Matthew"]["wins"] == 0


def test_new_player_starts_with_zero_losses():
    game_stats.clear()

    add_player("Matthew")

    assert game_stats["Matthew"]["losses"] == 0


def test_new_player_starts_with_zero_ties():
    game_stats.clear()

    add_player("Matthew")

    assert game_stats["Matthew"]["ties"] == 0


def test_total_games():
    stats = {"wins": 5, "losses": 3, "ties": 2}

    assert get_total_games(stats) == 10


def test_win_rate():
    stats = {
        "wins": 8,
        "losses": 1,
        "ties": 1,
    }

    assert get_win_rate(stats) == 80


def test_win_rate_no_games():
    stats = {
        "wins": 0,
        "losses": 0,
        "ties": 0,
    }

    assert get_win_rate(stats) == 0
