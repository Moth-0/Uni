'''
    DECREASING

    Report all indices (i, j) of positive entries in an n x n matrix in 
    decreasing order of the values of the entries of the matrix, where i is the 
    row index and j is the column index, 0 <= i < n and 0 <= j < n.

    E.g., for the matrix

         3  5  0
        -1  7  2
        -2  1  0
    
    there are five positive entries 7 5 3 2 1, and the output should consist 
    of the corresponding five indices (1, 1) (0, 1) (0, 0) (1, 2) (2, 1).

    Input:  A single line with a list-of-lists of integers representing a matrix.
            It is guaranteed that all positive entries are distinct, and that it
            is an n x n matrix, for 1 <= n <= 10

    Output: All entries (i, j) in the matrix containing a positive value in 
            decreasing value order, one pair per line. 

    Example: 

      Input:  [[3, 5, 0], [-1, 7, 2], [-2, 1, 0]]

      Output: (1, 1)
              (0, 1)
              (0, 0)
              (1, 2)
              (2, 1)

      The largest positive value is 7 at (1, 1), followed by 5 at (0, 1), ...

    Note: The below code already reads the matrix.
'''


matrix = eval(input())
# insert code
dic = {}
x = 0
y = 0
for row in matrix:
    for num in row: 
        if num > 0: 
            dic[num] = (x, y)
        y += 1
    y = 0
    x += 1

dic_sort = dict(reversed(sorted(dic.items()))) # This line is from https://stackoverflow.com/questions/9001509/how-do-i-sort-a-dictionary-by-key
for key in dic_sort: 
    print(dic_sort[key])
