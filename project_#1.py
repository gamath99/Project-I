""" Project 1
Gama Mathurin 
The count and capture Game 
The game consist in collecting more points then the opponents while moving the points in a clockwise way. The Player score by adding a point in 3 point cell.
"""

#Declare the main variable that will be used through all the program

#Declare variable that will store the score of each player 
player1_score = 0
player2_score = 0

# Assign the initial Board that will start the game
board = [[4,4],[4,4],[4,4]]

# Assign a variable for the turn player, 1 for player 1 and 2 for player 2
turn_player = 1

#Create a path on how to move the points in the board 
path = [(0,0),
        (0,1),
        (1,1),
        (2,1),
        (2,0),
        (1,0)
]

game_over = False

#The game is a counting and repetition process to capture points to score. 
# create a loop to play the game while consider the turn for each player 

while game_over == False:
    # Display the initial board 
    print("\nToukay Board")
    print("---------------------------")
    print("|Row|    |P1|    |P2|")
    
    for i in range(len(board)):
        print("----------------------")
        print("|",i,"|", "    ", "|",board[i][0],"|", "    ", "|",board[i][1],"|")
        print("----------------------")

    print("\nScores")
    print("Player 1:", player1_score)
    print("Player 2:", player2_score)
    
    #Check if the board is empty, meanwhile the game is over if it is empty
    total = 0

    for row in board:
        total += row[0] + row[1]
        
    if total == 0:
        game_over = True
        break

    print("\nPlayer", turn_player)

    row_selection = int(input("Choose row(0-2): "))
    col_selection = 0

    #Identify the column of each player 
    if turn_player == 1: 
        Col_selection = 0
    else:
        col_selection = 1
    
    #validate move by evaluate the player input
    if row_selection < 0 or row_selection > 2:
        print("Please select another row between (0-2)")
    
    elif board[row_selection][col_selection] == 0:
        print(" That cell is empty.")

    else: 
        turn_over = False 
        while turn_over == False:
            stones = board[row_selection][col_selection]
            board[row_selection][col_selection] = 0 

            index = path.index((row_selection, col_selection))

            was_empty = False

            #designated player distribute the stones in the board. 
            while stones > 0:

                index = (index + 1) % len(path)

                r = path[index][0]
                c = path[index][1]

                if stones == 1 and board[r][c] == 0:
                    was_empty = True

                board[r][c] += 1 

                stones -= 1

            #Capture the stones by the current player 

            captures = 0

            if board[r][c] == 4:

                board[r][c] = 0

                captures += 1 

                if turn_player == 1:
                    player1_score += 4
                else:
                    player2_score += 4

                previous_index = (index - 1) % len(path)


                r2 = path[index][0]
                c2 = path[index][1]

                if board[r2][c2] == 4 and captures < 2:
                    board[r2][c2] = 0

                    captures += 1
                           
                    if turn_player == 1:
                        player1_score += 4
                    else:
                        player2_score += 4

            #print("Capture!!!")

            # continue collecting stones or stop 

            if was_empty:

                turn_over = True
            else:
                pass    
                #row_selection = r
                #col_selection = c

                #print("Continue picking stones from cell:", row_selection, col_selection)

    #Change player
    if turn_player == 1:
        turn_player = 2
    else:
        turn_player = 1

print("Game Over")

print("Player 1:", player1_score)
print("Player 2:", player2_score)

if player1_score >player2_score:
    print("Player 1 wins!")

elif player2_score > player1_score:
    print("Player 2 wins!")

else:
    print("Draw!")



    





