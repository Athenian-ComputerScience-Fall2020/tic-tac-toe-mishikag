# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  none
# A note on style: Dictionaries can be defined before or after functions.

board = {'TL': ' ' , 'TM': ' ' , 'TR': ' ' ,'ML': ' ' , 'MM': ' ' , 'MR': ' ' ,'BL': ' ' , 'BM': ' ' , 'BR': ' ' }

def gameboard(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def main():
    player = 'X'
    num = 0

    for i in range(10):
        gameboard(board)
        print("It is player " + player + "'s turn. " + player + ", what do you want to move? Use the keys: TL, TM ,TR, ML, MM, MR, BL, BM, BR, to pick a spot on the board: ")

        move = input()

        if board[move] == ' ':
            board[move] = player
            num += 1
        else:
            print("That spot is already filled. pick another move")
            continue

        if num >= 5:
            if board['TL'] == board['TM'] == board['TR'] != ' ':
                gameboard(board)
                print(player + " won.")
                break

            elif board['ML'] == board['MM'] == board['MR'] != ' ':
                gameboard(board)
                print(player + " won.")
                break

            elif board['BL'] == board['BM'] == board['BR'] != ' ':
                gameboard(board)
                print(player + " won.")
                break

            elif board['TL'] == board['ML'] == board['BL'] != ' ':
                gameboard(board)
                print(player + " won.")
                break

            elif board['TM'] == board['MM'] == board['BM'] != ' ':
                gameboard(board)
                print(player + " won.")
                break

            elif board['TR'] == board['MR'] == board['BR'] != ' ':
                gameboard(board)
                print(player + " won.")
                break

            elif board['TL'] == board['MM'] == board['BR'] != ' ':
                gameboard(board)
                print(player + " won.")
                break

            elif board['TR'] == board['MM'] == board['BL'] != ' ':
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
main()
