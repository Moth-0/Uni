'''
    FREQUENT

    Print the most frequent integer(s) occurring in a list of integers.

    Input:  A single line with n space separated positive integers,
            where 1 <= n <= 100.

    Output: If the most frequent integer(s) occur x times in the input,
            print all integers occurring x times in the input,
            one integer per line, and in increasing order.

    Example:

      Input:  1 2 2 300 2 5 5 300 4 4 4 4 1 2

      Output: 2
              4
'''


# insert code
from collections import Counter

numbers = map(int, input().split())

count = Counter(numbers)

for x in sorted(count.keys()): 
    if count[x] == max(count.values()):
        print(x)