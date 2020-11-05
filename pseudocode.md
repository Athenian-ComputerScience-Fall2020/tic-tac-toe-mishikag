* Dictionary definiton (the_board)
    * Keys: TL, TM TR, ML, MM, MR, BL, BM, BR
    * Values: are empty spaces

* define the function "real_board" with dictionary "the_board" as a parameter
    * print the board

* define the function "game"
    * the variable a equals player X because X goes first
    * count is equal to 0

    * for i in the range of 10:
        * call the function real_board with parameter the_board
        * print whose turn it is

        * move is equal to an input
            * this input is for the user to enter their move

        * if the block that the user requested is empty
            * fill that block with the user X or O depending on whose turn it is
            * add one to count

        * else if it is filled or not empty
            * print that the spot is filled
            * continue the code

        # this is to switch user X and player O
        * if player is equal to X
            * make player equal to O to switch user
        * else
            * player is equal to user X

        # this is to check the winning conditions
        ## least amount of moves you can use to win is 5, so it will start checking these conditions after 5 moves have passed
        * if count is greater than or equal to 5:
            * if a three in a row or diagonal are equal to each other in the board
                * print the board
                * print who won the game
                * break out of code
            * code checks for every possible winning solution

        # if the board is full
        * if count is equal to 9
            * print that it is a tie
* call the function main
