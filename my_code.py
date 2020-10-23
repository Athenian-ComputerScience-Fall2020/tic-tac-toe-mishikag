# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
# A note on style: Dictionaries can be defined before or after functions.

the_board = {'TL': ' ','TM': ' ','TR': ' ','ML': ' ','MM': ' ','MR': ' ','BL': ' ','BM': ' ','BR': ' '}

def display_board(theBoard):
    print(theBoard['TL'], '  |',theBoard['TM'], ' |', '  ',theBoard['TR'])
    print ('-+-+-'+'-+-+-'+'-+-+-')
    print(theBoard['ML'], '  |',theBoard['MM'], ' |', '  ',theBoard['MR'])
    print ('-+-+-'+'-+-+-'+'-+-+-')
    print(theBoard['BL'], '  |',theBoard['BM'], ' |', '  ',theBoard['BR'])
    print ('-+-+-'+'-+-+-'+'-+-+-')

#def intro_board(theBoard):
    #print ('|    ' '|    ' '|    ')
    #print ('-+-+-'+'-+-+-'+'-+-+-')
    #print ('|    ' '|    ' '|    ')
    #print ('-+-+-'+'-+-+-'+'-+-+-')
    #print ('|    ' '|    ' '|    ')
    #print ('-+-+-'+'-+-+-'+'-+-+-')

def CheckWinner(the_board):
    global check
    check = 0
    #use different board
    if the_board['Tl'] == the_board['TM'] == the_board['TR'] != ' ' :
        check = 1
    elif the_board['TL'] == the_board['ML'] == the_board['BL'] != ' ':
        check = 1
    elif the_board['TL'] == the_board['MM'] == the_board['BR'] != ' ':
        check = 1
    elif the_board['ML'] == the_board['MM'] == the_board['MR'] != ' ':
        check = 1
    elif the_board['BL'] == the_board['BM'] == the_board['BR'] != ' ':
        check = 1
    elif the_board['BL'] == the_board['MM'] == the_board['TR'] != ' ':
        check = 1
    elif the_board['TR'] == the_board['MR'] == the_board['BR'] != ' ':
        check = 1
    elif the_board['BM'] == the_board['MM'] == the_board['TM'] != ' ':
        check = 1
    return check

def game(the_board):
    a = "X"
    for i in range(9):
        display_board(the_board)
        print("it is", a, "turn")
        turns = input("enter a place in the board")
        while True:
            if the_board[turns]==' ':
                the_board[turns] == a
                break
            else:
                print("sorry this spot is already taken. place your", a, "somewehere else")
                display_board(the_board)
                turns = input("enter a place in the board")
            check == CheckWinner(the_board)
            if check == 1:
                print("the winner is", a)
                break
            else:
                print("there is no winner")
                break
game(the_board)
display_board(the_board)
