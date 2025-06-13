'''
    MARKS

    Write a function marks(L) that takes a list of pairs (symbol, count)
    and for each pair prints a line with count copies of symbol, e.g.,

        marks([('A', 10), ('B', 5), ('C', 15)])

    should print the three lines

        AAAAAAAAAA
        BBBBB
        CCCCCCCCCCCCCCC

    Input:  A single line containing a Python list of pairs (symbol, count).
            The length contains between 1 and 100 pairs, each count is an 
            integer between 1 and 100, and symbol is a string of length 1.  
            All symbols are distinct.

    Output: One line for each pair (symbol, count) in the input list,
            containing count copies of symbol (and no other character).

    Example:
    
      Input:  [('A', 10), ('B', 5), ('C', 15)]

      Output: AAAAAAAAAA
              BBBBB
              CCCCCCCCCCCCCCC

    Note: The below code already reads the input and calls the marks function.
'''


def marks(L):
    # insert code
    for t in L: 
        print(f"{t[0]*t[1]}")


marks(eval(input()))
