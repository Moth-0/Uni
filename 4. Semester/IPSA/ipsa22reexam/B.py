'''
    POWER SUM

    For two positive integers x and p print x ** 1 + x ** 2 + ... + x ** p.
    E.g. for x = 3 and p = 5 the value 363 should be printed, since

          3 ** 1 + 3 ** 2 + 3 ** 3 + 3 ** 4 + 3 ** 5
        = 3 + 9 + 27 + 81 + 243
        = 363

    Input:  A single line with two space separated integers x and p,
            where 1 <= x <= 100 and 1 <= p <= 100.

    Output: A single line with the sum x ** 1 + x ** 2 + ... + x ** p.

    Example:

      Input:  3 5

      Output: 363

    Note: The below code already handles reading the input.
'''


x, p = map(int, input().split())
sum = 0

# insert code
while p > 0: 
    sum += x**p
    p -= 1

print(sum)
