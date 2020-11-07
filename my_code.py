# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  none
# A note on style: Dictionaries can be defined before or after functions.

board = {'1': ' ' , '2': ' ' , '3': ' ' ,'4': ' ' , '5': ' ' , '6': ' ' ,'7': ' ' , '8': ' ' , '9': ' ' }

def gameboard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def main():
    player = 'X'
    num = 0

    for i in range(10):
        gameboard(board)
        print("It is player " + player + "'s turn. " + player + ", what do you want to move? Use the keys: 1, 2, 3, 4, 5, 6, 7, 8, 9 to pick a spot on the board: ")

        move = input()

        if board[move] == ' ':
            board[move] = player
            num += 1
        else:
            print("That spot is already filled. pick another move")
            continue

        if num >= 5:
            if board['1'] == board['2'] == board['3'] != ' ':
                gameboard(board)
                print(player + " won.")
                break

            elif board['4'] == board['5'] == board['6'] != ' ':
                gameboard(board)
                print(player + " won.")
                break

            elif board['7'] == board['8'] == board['9'] != ' ':
                gameboard(board)
                print(player + " won.")
                break

            elif board['1'] == board['4'] == board['7'] != ' ':
                gameboard(board)
                print(player + " won.")
                break

            elif board['2'] == board['5'] == board['8'] != ' ':
                gameboard(board)
                print(player + " won.")
                break

            elif board['3'] == board['6'] == board['9'] != ' ':
                gameboard(board)
                print(player + " won.")
                break

            elif board['1'] == board['5'] == board['9'] != ' ':
                gameboard(board)
                print(player + " won.")
                break

            elif board['3'] == board['5'] == board['7'] != ' ':
                gameboard(board)
                print(player + " won.")
                break

        if player =='X':
            player = 'O'
        else:
            player = 'X'

        if num == 9:
            gameboard(board)
            print("It's a Tie!!")
            break
try:
    main()
except:
    print("bad input")
    main()
