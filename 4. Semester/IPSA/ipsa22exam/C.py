'''
    BLOCK

    Write a program that prints a rectangular block with the same symbol.
    The program should read three lines: the first line the number of
    rows to output, the second line the number of columns to output,
    and the last line the symbol to repeat rows * columns times.
 
    Input:  1st line the integer rows (1 <= rows <= 25).
            2nd line the integer columns (1 <= columns <= 25).
            3rd line the single printable character symbol (not whitespace).

    Output: rows lines each with columns copies of symbol.

    Example:

      Input:  3
              5
              x

      Output: xxxxx
              xxxxx
              xxxxx
'''


# insert code
rows = int(input())
col = int(input())
symbol = input()

for r in range(rows):
    print(col*symbol)

