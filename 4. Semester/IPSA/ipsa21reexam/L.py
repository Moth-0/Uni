r'''
    FLIPPER

    Your task is to mark the trace of a ball on a rectangular board,
    where the ball can bounce off diagonal walls. 

    The ball is initially moving in one of the four directions:
    up = '^', down = 'v', left = '<' or right = '>'. On the board there
    are a set of diagonal walls marked '\' and '/', where the ball will
    change direction. E.g. when the ball is moving '>' (right) and hits '\'
    it will change direction to 'v' (down). See example below. The ball
    will eventually leave the board or enter an infinite cycle.

    Input:  The first line contains two integers rows and columns,
            separated by space, where 1 <= rows <= 25 and 1 <= columns <= 25.
            The following rows lines contains columns symbols, from '.\/<>^v'.
            There will be exactly one symbol from '<>^v' in total, being
            the start position and direction of the ball. '.' are free cells.
            No two wall symbols from '\/' will be adjacent.

    Output: The trace of the ball, i.e. the last rows lines from the input,
            except that all free cells visited by the ball should
            be marked '*', including the starting position.

    Example:

      Input:  10 20
              ....................
              ....................
              .......>........\...
              ....................
              ....................
              ....................
              ....................
              ....................
              ................/...
              ....................
    
      Output: ....................
              ....................
              .......*********\...
              ................*...
              ................*...
              ................*...
              ................*...
              ................*...
              ****************/...
              ....................
'''


# insert code
rows, cols = map(int, input().split())

board = [list(input()) for _ in range(rows)]

direction = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}

flip = {'>/': '^', '</': 'v', 'v/': '<', '^/': '>',
        '>\\': 'v', '<\\': '^', 'v\\': '>', '^\\': '<'}

for i, row in enumerate(board):
    for j, symbol in enumerate(row):
        if symbol in direction:
            x, y, d = j, i, symbol

for _ in range(2 * rows * cols): 
    if 0 <= y < rows and 0 <= x < cols: 
        board[y][x] = "*"
        dx, dy = direction[d]
        x, y = x + dx, y + dy
        if 0 <= y < rows and 0 <= x < cols and board[y][x] in '\\/':
            d = flip[d + board[y][x]]
            dx, dy = direction[d]
            x, y = x + dx, y + dy

for row in board:
    print(''.join(row))