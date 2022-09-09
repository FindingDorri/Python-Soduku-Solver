board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

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
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)

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
    
    # Check box
    box_pos_x = empty_position[1] // 3
    box_pos_y = empty_position[0] // 3

    pass
print_board(board)