
from random import randint

game_array = []

player_one = {
    "name": "Player 1",
    "wins": 0,
}

player_two = {
    "name": "Player 2",
    "wins": 0,
}

colors = {
    "reset":"\033[00m",
    "black":"\033[90m",
    "blue":"\033[94m",
    "cyan":"\033[96m",
}

# building the board
def build_game_board(board):
    size=5
    for item in range(size):
        board.append(["O"] * size)


def display(board):
    for row in board:
        print(" ".join(row))

# Defining ship locations
def load(board):
    print("Welcome to the game of BATTLESHIP!")
    print("Find and sink the ship!")
    del board[:]
    build_game_board(board)
    print(colors['blue'])
    display(board)
    print(colors['reset'])
    column = randint(1, len(board))
    row = randint(1, len(board[0]))
    return {
        'column': column,
        'row': row,
    }

ship_points = load(game_array)

# Alternating turns
def player_turns(total_turns):

    if total_turns % 2 == 0:
        total_turns += 1
        return player_one

    return player_two

# Restart game
def restart():


    global ship_points

    while True:
        answer = input("Play again? [yes / no]: ").lower().strip()
        if answer == "yes":
            ship_points = load(game_array)
            main()
            break

        elif answer == "no":
            print("Thanks for playing!")
            exit()

# game playing
def guess(row, column, player, board):
    guess_col = 0
    guess_row = 0
    while True:

        try:
            guess_row = int(input("Guess Row:")) - 1
            guess_col = int(input("Guess Col:")) - 1
        except ValueError:

            print("Invalid input, please enter a digit: ")
            continue
        else:

            break
    match = guess_row == row - 1 and guess_col == column - 1
    not_found = (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4)

    if match:
        player["wins"] += 1
        print("Congratulations! You sunk my battleship!")
        print('The current match score is %d : %d (Player1 : Player2)' % (player_one["wins"], player_two["wins"]))
        print("Game Over!")
        restart()

    elif not match:
        if not_found:
            print("Oop,That's not even in the ocean!")

        elif board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "Y":
            print("That's been done already!")

        else:
            print("Missed")
            if player == player_one:
                board[guess_row][guess_col] = "X"
            else:
                board[guess_row][guess_col] = "Y"

        print(colors['cyan'])
        display(game_array)
        print(colors['reset'])

    else:
        return 0


begin = input("Type 'start' to begin: ")

while (begin != str('start')):
    begin = input("Type 'start' to begin: ")

def main():

    for chances in range(6):

        if player_turns(chances) == player_one:
            print(ship_points)
            print("Player One")
            guess(
                ship_points['row'],
                ship_points['column'],
                player_one, game_array
            )

        elif player_turns(chances) == player_two:
            print("Player Two")
            guess(
                ship_points['row'],
                ship_points['column'],
                player_two, game_array
            )

        if chances == 5:
            print("It's a draw.")
            print(colors['black'])
            display(game_array)
            print(colors['reset'])
            print('Current Score is %d : %d (Player1 : Player2)' % (player_one["wins"], player_two["wins"]))
            restart()

if __name__ == "__main__":
    main()