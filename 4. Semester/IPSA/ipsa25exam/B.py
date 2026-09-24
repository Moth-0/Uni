'''
    SORT LINES

    Input:  The first line contains an integer n, 1 <= n <= 10. Each of the 
            following n line contains a string consisting of between 1 and 25 
            capital letters.

    Output: The n lines sorted in alphabetic order.

    Example:

      Input:  3         
              PETER
              ANDERS
              CASPER

      Output: ANDERS
              CASPER
              PETER
'''


# insert code
n = int(input())

names = [input() for _ in range(n)]

out = sorted(names)

for n in out:
    print(n)
