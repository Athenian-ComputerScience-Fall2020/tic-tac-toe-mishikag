# Pseudocode for this program
(this can be in a flowchart, using bullet points, inserting a picture, etc)

* Dictionary definiton (the_board)
    * Keys: TL, TM TR, ML, MM, MR, BL, BM, BR
    * Values: are empty spaces

* define the function "real_board" with dictionary "the_board" as a parameter
    * print the board

* define the function "game"
    * the variable a equals X
    count is equal to 0

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

        # this is to check the winning conditions
        * it checks it every time after 5 moves (need at least 5 moves to win)
        * if count is greater than or equal to 5:
            * if a three in a row or diagonal are equal to each other in the board
                * print who won
                * break out of code
                    * whoever played the last move is who won
            * code checks for every possible winning solution

        # if the board is full
        * if count is equal to 9
            * print that it is a tie






Below are templates for flowcharts and mardown. feel free to edit them - or delete them and do something else if you prefer.

# Markdown


## Markdown
This is a brief guide to Markdown. Click the edit button to see what to type and use the "Preview changes" tab to check your work as you go.

# Heading1
## Heading 2
### Heading 3

* Point 1
  * Point 2 (tabbed over)
    * Point 3 (tabbed over from line above)

*italics*
**bold**


