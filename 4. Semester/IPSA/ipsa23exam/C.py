'''
    EXTREME

    You are given a table of n x n numbers. An "extreme" number is a number 
    that is both the largest number in its row and the smallest number 
    in its column. In the example below, 5 is an extreme number, since it
    is the largest in row 2 and the smallest in column 1 (assuming rows
    and columns are numbered from 0).

        3 6 2
        7 9 8
        1 5 4

    Your task is to write a function extreme(table) that takes a table 
    represented by a list of lists of integers and returns the position of 
    an extreme number, if one exists. Otherwise it should return (-1, -1).

    Input: The first line contains an integer n, the dimension of the table.
           The next n lines contain n integers each, representing the table.
           It is guaranteed that the numbers in the table are the distinct
           integers 1 .. n ** 2, and 1 <= n <= 25.

    Ouput: The tuple (i, j) if table[i][j] is an extreme number. 
           If no extreme number exists, output (-1, -1).
           It is guaranteed that there is at most one extreme number.

    Example:

      Input:  3
              3 6 2
              7 9 8
              1 5 4

      Output: (2, 1)

    Note: The below code already reads the input table into a 
          list-of-lists representation and calls the extreme function.
'''


def extreme(table):
    # insert code
    for i in range(n): 
        for j in range(n): 
            if max(table[i]) == min([table[y][j] for y in range(n)]):
                return (i, j)
    return (-1, -1)



n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
print(extreme(table))
