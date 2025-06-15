'''
    ECHO

    Your task is to print a word repeated n times.

    Input:  Two lines.
            First line contains a word with 1 to 25 capital letters.
            The second line contains an integer n, 1 <= n <= 10.

    Output: n lines each containing the word.

    Example:

       Input:  ECHO
               3

       Output: ECHO
               ECHO
               ECHO

    Note: The below code already handles reading the input.
'''


word = input()
n = int(input())

# insert code

for _ in range(n):
    print(word)
