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

#The game is a counting and repetition process to capture points to score. 
# create a loop to play the game while consider the turn for each player 

while True:
    # Display the initial board 
    print("\nToukay Board")
    print("Row  Player_1    Player_2")

    for i in range(len(board)):
        print(i, "  ", board[i][0], "   ", board[i][1])

    print("\nScores")
    print("Player 1:", player1_score)
    print("Player 2:", player2_score)
    
    #Check if the board is empty as the game is over if it is empty
    total = 0

    for row in board:
        total += row[0] + row[1]
        
    if total == 0:
        break

    print("\nPlayer", turn_player)

    row_selection = int(input("Choose row(0-2): "))

    #Identify the column of each player 
    if turn_player == 1: 
        Col_selection = 0
    else:
        col_choice = 1

    





    
