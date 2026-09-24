'''
    SQUARE BOARD

    Your task is to print an n x n board alternating between two symbols in the
    rows and columns (like an 8 x 8 chessboard alternating between white and 
    black).
    
    Input:  A single line containing three space separated values: an integer n 
            and two single characters a and b, where 1 <= n <= 25.
    
    Output: n lines, each line containing n characters. The rows and columns
            should alternative between containing a and b, and the top-left 
            symbol should be a.

    Example:

      Input:  5 X -
              01234
      Output: X-X-X 0 
              -X-X- 1
              X-X-X 2
              -X-X- 3
              X-X-X 4
'''


# insert code
n, a, b = input().split()
n = int(n)

for i in range(n): # Rows
    print("".join([a if (i+j) % 2 == 0 # a on even
                   else b for j in range(n)])) 
