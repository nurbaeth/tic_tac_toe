import pytest
from tic_tac_toe import check_winner, is_full

def test_check_winner():
    board_x_wins = [
        ["X", "X", "X"],
        ["O", "O", " "],
        [" ", " ", " "]
    ]
    assert check_winner(board_x_wins, "X") == True
    assert check_winner(board_x_wins, "O") == False

def test_is_full():
    full_board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"]
    ]
    empty_board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    assert is_full(full_board) == True
    assert is_full(empty_board) == False
