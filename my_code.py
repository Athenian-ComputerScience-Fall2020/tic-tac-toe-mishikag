# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
# A note on style: Dictionaries can be defined before or after functions.

the_board = {'TL': ' ' , 'TM': ' ' , 'TR': ' ' ,
            'ML': ' ' , 'MM': ' ' , 'MR': ' ' ,
            'BL': ' ' , 'BM': ' ' , 'BR': ' ' }

def real_board(the_board):
    print(the_board['TL'] + '|' + the_board['TM'] + '|' + the_board['TR'])
    print('-+-+-')
    print(the_board['ML'] + '|' + the_board['MM'] + '|' + the_board['MR'])
    print('-+-+-')
    print(the_board['BL'] + '|' + the_board['BM'] + '|' + the_board['BR'])

def main():
    a = 'X'
    count = 0

    for i in range(10):
        real_board(the_board)
        print("It is player " + a + "'s turn." + a + ", what do you want to move?")

        move = input()

        if the_board[move] == ' ':
            the_board[move] = a
            count += 1
        else:
            print("That place is already filled. pick another move")
            continue

        if count >= 5:
            if the_board['TL'] == the_board['TM'] == the_board['TR'] != ' ':
                real_board(the_board)
                print(a + " won.")
                break

            elif the_board['ML'] == the_board['MM'] == the_board['MR'] != ' ':
                real_board(the_board)
                print(a + " won.")
                break

            elif the_board['BL'] == the_board['BM'] == the_board['BR'] != ' ':
                real_board(the_board)
                print(a + " won.")
                break

            elif the_board['TL'] == the_board['ML'] == the_board['BL'] != ' ':
                real_board(the_board)
                print(a + " won.")
                break

            elif the_board['TM'] == the_board['MM'] == the_board['BM'] != ' ':
                real_board(the_board)
                print(a + " won.")
                break

            elif the_board['TR'] == the_board['MR'] == the_board['BR'] != ' ':
                real_board(the_board)
                print(all + " won.")
                break

            # finish conditions

        if count == 9:
            real_board(the_board)
            print("It's a Tie!!")
            break

main()
