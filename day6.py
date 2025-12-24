# Display the board
def show(board):
    print()
    for i in range(0, 9, 3):
        print(board[i], board[i+1], board[i+2])
    print()


# Check winning condition
def check_win(board, player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]             # diagonals
    ]

    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == player:
            return True
    return False


# Player choice
def choose(player, board, choices):
    pos = int(input(f"Player {player}, choose position {choices}: "))

    if pos in choices:
        choices.remove(pos)
        board[pos - 1] = player
        show(board)
        return check_win(board, player)
    else:
        print("Invalid position!")
        return False


# Main program
board = ["-"] * 9
choices = list(range(1, 10))
turn = 0
winner = "Game Tie"

show(board)

while choices:
    player = "X" if turn % 2 == 0 else "O"

    if choose(player, board, choices):
        winner = f"Winner is Player {player}"
        break

    turn += 1

print(winner)
print("Game Over")