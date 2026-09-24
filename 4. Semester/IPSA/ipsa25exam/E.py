'''
    BOUNDING BOX

    Input to this problem is an n x m-matrix containing 0-1 values, where rows 
    are numbered 0 to n-1 and columns 0 to m - 1, and the top-left is row 0 
    and column 0. Your task is to compute a bounding box of the '1's in the 
    matrix, i.e., the minimum and maximum row numbers i_min and i_max, where 
    there is a '1' in the row, and similarly the leftmost and rightmost columns 
    j_min and j_max, where there is a '1' in the column.

    Input:  The first line contains two integers n amd m separated by space,
            where 1 <= n <= 50 and 1 <= m <= 50. The next n lines contains
            m characters, each being '0' or '1', representing an n x m-matrix.
            The matrix contains at least one '1'.

    Output: A single line with the four integers i_min, j_min, i_max and j_max 
            separated by spaces.

    Example:

      Input:  8 10
              0000000000
              0000110000
              0001111000
              0011111100
              0011111100
              0011111100
              0000000000
              0000000000

      Output: 1 2 5 7

      Illustration of output (input has rows 0..7 and columns 0..9): 
            
              0123456789

           0  0000000000
           1  0000110000  <-- i_min = 1
           2  0001111000
           3  0011111100
           4  0011111100
           5  0011111100  <-- i_max = 5
           6  0000000000
           7  0000000000
                ^    ^
         j_min = 2  j_max = 7
'''


# insert code
n, m = map(int, input().split())

board = [[x for x in input()] for _ in range(n)]
# input() = "0","0","0", 0000"
# A list of lists every row is a list of individual strings 
# [["0", "0", "1", "0"], [...], ...]

i_list = []
j_list = []

# makes column and row list containing index containing ones. 
for i in range(n):
    for j in range(m):
        if board[i][j] == "1": 
            i_list.append(i)
            j_list.append(j)

print(f"{min(i_list)} {min(j_list)} {max(i_list)} {max(j_list)}") 