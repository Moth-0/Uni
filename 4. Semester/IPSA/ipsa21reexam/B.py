'''
    DIAGONAL WORD

    Your task is to read a word from input and to print the word 
    diagonally in a square otherwise filled with '.'.

    Input:  A single line containing a string with 1 <= length <= 25 symbols,
            and all symbols being characters 'a'-'z' and 'A'-'Z'

    Output: Print length lines, each containing length symbols, all
            symbols being '.', except the diagonal top-left to bottom-right
            that should contain the input string.

    Example:

       Input:  Python

       Output: P.....
               .y....
               ..t...
               ...h..
               ....o.
               .....n
'''


# insert code

word = input()
n = len(word)

for i in range(n): 
    print(i*'.' + word[i] + (n-i-1)*'.')
