'''
    WATER

    Assume we model a rectangular n x m terrain as a set of square cells and for
    each cell store its height in a matrix, where the height of a cell is an
    integer between 0 and 9. The following 5 x 8-matrix represents a terrain.

        44455599
        52344349
        51538459
        50029329
        55067999

    We assume the rows of the matrix are numbered top-down 0 to n-1, and columns
    left-to-right 0 to m-1. 
    
    Assume we pour water onto one of the cells, e.g., cell (2, 4) in the above 
    terrain (the unique cell with height 8). Your task is to identify the cells 
    where the water can flow to, under the assumption that water can flow 
    directly from a cell to its vertical and horizontal neighbors in the matrix, 
    provided that these are not higher (water cannot flow directly to a diagonal 
    cell that is only connected to the cell at a corner; water can also not 
    flow outside the rectangular terrain considered).

    If we mark all cells where water can flow to by '*' in the above terrain 
    when we pour water on the cell (2, 4), we get the following terrain.

        44455599
        5*****49
        5*5***59
        5***9**9
        55*67999

    Input:  The first line contains four space separated integers n, m, i and j,
            where 3 <= n <= 20, 3 <= m <= 40, 0 <= i < n and 0 <= j < m.
            The following n lines each contain m digits, representing the 
            heights of the cells in the terrain.

    Output: The same terrain, except that cells where water can flow to from 
            the cell (i, j) are replaced by '*'.

    Example:

      Input:  5 8 2 4
              44455599
              52344349
              51538459
              50029329
              55067999

      Output: 44455599
              5*****49
              5*5***59
              5***9**9
              55*67999
'''


# insert code
from functools import cache
n, m, x, y = map(int, input().split())

board = [[p for p in input()] for _ in range(n)]
# board = [["4", "3", "2"], ...]

is_valid = set()
directions = [(0, 1), (0,-1), (1,0), (-1,0)]

@cache 
def valid(i, j): 
    # Add point to set of valid points
    is_valid.add((i, j))
    for d in directions: # Walk all directions from point 
        # Check direction is a valid step 
        if 0 <= i+d[0] < (n) and 0<= j+d[1] < (m):  
            # Makes valid skip repeats 
            if (i+d[0],j+d[1]) not in is_valid: 
                # If the water can flow in direction
                if board[i][j] >= board[i+d[0]][j+d[1]]: 
                    # Check from that direction
                    valid(i+d[0], j+d[1])
        
valid(x, y)

# Replace valid points with water marks 
for i in range(n): 
    for j in range(m):
        if (i, j) in is_valid: 
            board[i][j] = "*"

for row in board: 
    print("".join(map(str,row)))