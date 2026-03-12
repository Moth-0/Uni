### Hand in 5
## n Queen puzzle

'''
HANDIN 5 (eight queens puzzle)

This handin is done by:

    202106248 Matilde E. Hansen
    202105331 Elias R. Skjoldborg

Reflection upon solution:

For this solution, we started to look at a function, that could check if a position is valid by scanning the column for each row to check if it already contains a 
queen, and then checks if abs(r1 - r2) == abs (c1 - c2) for rows and columns. A much simpler way to execute this is by checking the positive diagonal and the 
negative diagonal from a queen position, aka (r + c) and (r - c). To explain with an example: If a position is in row 1 column 1, this gives a pos = 2 and neg = 0, 
such that when it checks for c = 2 or 0 it won't hits those positions. It does this over all columns c, such that two queens won't be diagonal to each other across 
the board. We make a board before the backtracking function as well, as an array of dots. We wanted to check positions for each row (r), running from r = 0 to 
r = n-1, and for each row check all the columns and the diagonals. This way, we automatically only place one queen in each row. In the backtracking function we 
wrote an if-statement, that checks if a position is valid, which continues untill if finds a valid position. We use .add to add a valid position in each set 
(col, pos and neg) and replace a dot with a queen for that position. Recursively we call the backtracking function again, and add one row to the function. 
In order for the new backtracking function to work as intended, we needed to remove the valid position in the column set and the diagonal sets again, as it is for 
the new row, not valid anymore. Therefore we also replace that position with a dot, otherwise the code would just print more and more queens the more solutions 
were printed. From the maze task (9.3) we used the code to print the boards as a string with n lines.   

'''

def Queen(n):
    col = set()                                                 # Creating a set of columns
    pos = set()                                                 # creating a set of positions on the positive diagonal
    neg = set()
    result = []
    board = [[". "] * n for i in range(n)]                       # Board created one row at a time

    def Backtrack(r):
        if r == n:
            board_copy = ["".join(row) for row in board]
            result.append(board_copy)
            
            return True
        for c in range(n):
            if c in col or (r + c) in pos or (r - c) in neg:    # for every column in a row we check if either a potential column position c is already in a column
                                                                # aka invalid position. Or if a potential position hits a diagonal from previous put positions
                continue                                        # If any of these positions are thus invalid for a queen to be placed, we continue, aka skip
                                                                # the position
            col.add(c)                                          # If the position is allowed, we add this c to the set of columns 
            pos.add(r + c)                                      # We also add the r + c position to the positive diagonal set
            neg.add(r - c)                                      # as well as the negative diagonal set
            board[r][c] = "Q "                                  # We thus place a queen in this valic r,c position
            
            Backtrack(r + 1)                                    # Now we use recursive backtracking, where we add a row to toe function, and the backtracking
                                                                # runs again
            col.remove(c)                                       # For the backtracking to run again, we need to clear it for the placed positions, as they are 
                                                                # not yet valid for the new row. Therefore we remove the positions again
            pos.remove(r + c)
            neg.remove(r - c)
            board[r][c] = ". "                                                   
            
    Backtrack(0)
    if len(result) == 0:
        print('There is no solution')
    return result

## code from task 9.3 (the maze task)
def matrix_to_string(Matrix):
    matrix_string = ''
    for line in Matrix:
        for j in line:
            matrix_string += j[0]
        matrix_string += '\n'
    return matrix_string
## 

n = int(input("Write dimension of chessboard here: "))

# Here 
sol = Queen(n)
for solution in sol:
    print(matrix_to_string(solution))

print('Number of solutions:', len(sol))