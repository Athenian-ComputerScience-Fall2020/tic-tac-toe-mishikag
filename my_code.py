# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
# A note on style: Dictionaries can be defined before or after functions.

board = {'Tl':' ','TM':' ','TR':' ','ML':' ','MM':' ','MR':' ','BL':' ','BM':' ','BR':' '}

def intro_board(board):
    print ('|    ' '|    ' '|    ')
    print ('-+-+-'+'-+-+-'+'-+-+-')
    print ('|    ' '|    ' '|    ')
    print ('-+-+-'+'-+-+-'+'-+-+-')
    print ('|    ' '|    ' '|    ')
    print ('-+-+-'+'-+-+-'+'-+-+-')

def CheckWinner(board):
    check = 0
    #use different board
    if board['Tl'] == board['TM'] == board['TR'] != ' ' :
        check = 1
    elif board['TL'] == board['ML'] == board['BL'] != ' ':
        check = 1
    elif board['TL'] == board['MM'] == board['BR'] != ' ':
        check = 1
    elif board['ML'] == board['MM'] == board['MR'] != ' ':
        check = 1
    elif board['BL'] == board['BM'] == board['BR'] != ' ':
        check = 1
    elif board['BL'] == board['MM'] == board['TR'] != ' ':
        check = 1
    elif board['TR'] == board['MR'] == board['BR'] != ' ':
        check = 1
    elif board['BM'] == board['MM'] == board['TM'] != ' ':
        check = 1
    return check

def play(board):
    a = "X"
    for i in range(9):
        # different function board to display spots taken
        print("it is", a, "turn")
        turns = input("enter a place in the board")
        while True:
            if board[turns]==' ':
                board[turns] == a
                break
            else:
                print("sorry this spot is already taken. place your", a, "somewehere else")
                # different function board to display spots taken
                turns = input("enter a place in the board")



print(intro_board(board))



