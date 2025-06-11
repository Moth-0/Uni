'''
    FLIPPING

    Consider a grid of size n x n, where each cell is either empty '.' or
    occupied 'x'.  You task is to perform d simulation steps. In each step a
    grid cell becomes 'x' if an odd number of neighboring cells on the grid 
    (up, down, left, right) are marked 'x' before the step. Otherwise,
    the cell becomes '.'. E.g., the below illustrates two simulation steps:

        .....       .....       ..x..
        .....       ..x..       .....
        ..x..  -->  .x.x.  -->  x...x
        .....       ..x..       .....
        .....       .....       ..x..
    
    Input:  First line an integer n (1 <= n <= 25), the size of the grid.
            The second line an integer d (1 <= d <= 10), the number of steps.
            The next n lines contains the grid, each line consisting of n 
            characters, which are either '.' or 'x'.

    Output: The grid after performing d simulation steps.

    Example:

      Input:  5
              2
              .....
              .....
              ..x..
              .....
              .....

      Output: ..x..
              .....
              x...x
              .....
              ..x..
'''


# insert code
n = int(input())
d = int(input())

grid = [list(input()) for _ in range(n)]

def marked_neighbors(grid, i ,j): 
    return sum(grid[i + di][j + dj] == 'x'
               for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1))
               if 0 <= i + di < n and 0 <= j + dj < n)

for _ in range(d):
    grid = [['.' if marked_neighbors(grid, i, j) % 2 == 0 else 'x' for j in range(n)] for i in range(n)]

for row in grid:
    print(''.join(row))
