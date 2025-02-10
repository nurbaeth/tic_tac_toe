# Tic-Tac-Toe Game in Python

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    while True:
        print_board(board)
        row, col = map(int, input(f"Player {players[turn]}, enter row and column (0-2): ").split())
        if board[row][col] == " ":
            board[row][col] = players[turn]
            if check_winner(board, players[turn]):
                print_board(board)
                print(f"Player {players[turn]} wins!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            turn = 1 - turn
        else:
            print("Cell already taken, try again!")

if __name__ == "__main__":
    tic_tac_toe()
