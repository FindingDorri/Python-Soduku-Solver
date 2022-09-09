from turtle import back


board = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
]


def back_track(board):
    empty_box = find_empty(board)

    # if no empty box is found, the sudoku is sovled
    if not empty_box:
        return True
    else:
        row,col = empty_box

    # loop all valid move (1-9)
    for guess in range(1,10):
        # check to see if guess is a valid solution
        if is_valid(board,guess,(row,col)):
            # add guess to board if valid
            board[row][col]=guess
            # recusrive call the backtrack algo to move on the the next empty box with a new valid move/guessed number  
            if back_track(board):
                return True
            # if we loop through all the move and none of them is valid, we back track and set our last guess to 0
            board[row][col] = 0
    return False

def print_board(board):
    for i in range(len(board)):
        # After every three row, print line
        if i % 3 == 0 and i!= 0:
            print("-----------------------")
        for j in range(len(board[0])):
            # After every column, print line
            if j % 3 == 0 and j!=0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")



def find_empty(board):
    """Return the row and col index of an empty box"""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    
    # empty box is not found
    return None

def is_valid(board,guess,empty_position):
    # Check row
    for i in range(len(board[0])):
        # if we find a value in that row is the same as the guessed number and the position of the value is not the same as the position of the guessed value, then our guess is invalid  
        if board[empty_position[0]][i] == guess and i != empty_position[1]:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][empty_position[1]] == guess and i != empty_position[0]:
            return False
    
    # Check sub box
    # if we divide the box by 3, we can find what sub box the box is in
    box_pos_x = empty_position[1] // 3
    box_pos_y = empty_position[0] // 3

    for i in range(box_pos_y * 3, box_pos_y * 3 +3):
        for j in range(box_pos_x * 3, box_pos_x * 3 +3):
            if board[i][j] == guess and (i,j) != empty_position:
                return False

    return True




print_board(board)
back_track(board)
print("")
print_board(board)