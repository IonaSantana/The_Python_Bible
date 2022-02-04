global board
board = ["   " for i in range(9)]
player1 = 'X'
player2 = '0'

def print_board():
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def is_victory():
    if (board[0] == board[1] and board[1] == board[2] and board[0]!="   ") or \
        (board[0] == board[3] and board[3] == board[6] and board[0]!="   ") or \
        (board[0] == board[4] and board[4] == board[8] and board[0]!="   "):
        return board[0]

    if (board[2] == board[5] and board[5] == board[8] and board[2]!="   ") or \
        (board[2] == board[4] and board[4] == board[6] and board[2]!="   "):
        return board[2]

    if board[3] == board[4] and board[4] == board[5] and board[3]!="   ":
        return board[3]

    if board[6] == board[7] and board[7] == board[8] and board[6]!="   ":
        return board[6]

    if board[1] == board[4] and board[4] == board[7] and board[1]!="   ":
        return board[1]
    
    return ' '

def get_win(char):
    resp = " " + player1 + " "
    if char == resp:
        return 'The winner is the player1'
    else:
        return 'The winner is the player2'

def get_result(result,cont):
    print(result)
    if result != ' ':
        return get_win(result)
    elif cont == 9:
        return 'Its a draw | Deu velha!!!'
    return ' '

def player_move(cont):
    print("Your turn player {}".format(cont%2 + 1))
    choice = int(input("Enter your move (1-9): ").strip())
    if cont % 2 == 0:
        simbol = player1
    else:
        simbol = player2

    if board[choice - 1] == "   ":
        board[choice - 1] = ' ' + simbol + ' '
    else:
        print()
        print("That space is taken!") 
    return choice
#start the game

def choice_simbol():
    choice = int(input("1 to start or -1 to end: ").strip())
    if choice == -1:
        return choice

    global player1, player2
    player1 = input("Player 1, choice your simbol - X or O: ").strip().upper()

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return choice

choice = choice_simbol()
cont = 0
result = ' '
win = ' '
while choice!=-1:
    
    if win != ' ':
        print(win)
        choice = choice_simbol()
        if choice == 1:      
            board = ["   " for i in range(9)]
            cont = 0
        else:
            break

    choice = player_move(cont)
    print_board()
    result = is_victory()
    win = get_result(result, cont)
    cont = cont + 1
    
