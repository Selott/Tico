board = [['', '', ''], ['', '', ''], ['', '', '']]

player_one = "A"
player_two = "B"


setup = True


def display(b = []):
    for row in b:
        print(row )

display(board)

def checkrows(b = []):
    for row in b:
        if row[0] == row[1] and row[1] == row[2] and row[0] != "":
            return True
    return False
def checkcolumns(b = []):
    for col in range(3):
        if b[0][col] == b[1][col] and b[1][col] == b[2][col] and b[0][col] != "":
            return True
    return False

def checkdiagonals(b = []):
    return (b[0][0] == b[1][1] and b[1][1] == b[2][2] and b[0][0] != "")\
           or (b[2][0] == b[1][1] and b[1][1] == b[0][2] and b[1][1] != "" )


def checkwin(b = []):
    return checkrows(b) or checkcolumns(b) or checkdiagonals(b)

def checktie(b = []):
    for row in range(3):
        for col in range(3):
            if b[row][col] == "":
                return False
    return not checkwin(b)

def handleturn(symbol, row, column):
    board[row][column] = symbol

while setup:
    symbol_one = input("Player 1, please enter your symbol! ")[0]
    symbol_two = input("Player 2, please enter your symbol! ")[0]
    if symbol_one == symbol_two:
        print("Error: Please re-enter your symbols!")
    else:
        player_one = symbol_one
        player_two = symbol_two
        del symbol_one, symbol_two
        setup = False

print(f"Welcome Player 1 ({player_one}) and Player 2 ({player_two}) to another round of Tico!")


current_player = player_one

while True:
    display(board)

    row, col = -1, -1
    while row == -1 or col == -1:
        try:
            row = int(input(f"Your turn, {current_player}! Please enter an empty row: "))
            col = int(input(f"Your turn, {current_player}! Please enter an empty column: "))

            if row > 3 or row < 1:
                print("Error: Invalid row!")
            row, col = row-1, col-1
        except ValueError:
            row, col = -1, -1
            print("Error: Invalid row!")
            continue
    if board[row][col] != "":
        print("Spot isn't empty! Rety!")
        continue
    else:
        handleturn(current_player, row, col)
        print()


    if(checkwin(board)):
        print(f"Congratulations {current_player}! You won.")
        break
    elif checktie(board):
        print(f"It's a tie!")
        break
    else:
        current_player = player_one if current_player == player_two else player_two