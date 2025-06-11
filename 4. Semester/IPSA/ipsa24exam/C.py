'''
    SQUARE SUM

    Write a function square_sum(a, b) that takes two integers a and b, a <= b, 
    and returns the sum of all squares x**2, where x is a positive integer 
    and a <= x**2 <= b.

    E.g., square_sum(100, 200) = 730, since 
    
        10 ** 2 = 100 
        11 ** 2 = 121 
        12 ** 2 = 144
        13 ** 2 = 169
        14 ** 2 = 196

        100 + 121 + 144 + 169 + 196 = 730.

    Input:  A single line containing two integers a and b, 
            where 1 <= a <= b <= 1_000_000_000.

    Output: The sum of all squares x**2, where x is an integer and a <= x**2 <= b.

    Example:

      Input:  100 200   

      Output: 730

    Note: The below code already reads a and b, and calls square_sum(a, b).
'''
import math

def square_sum(a, b):
    # insert code
    x = math.ceil(a**(1/2))
    sum = 0
    while x**2 <= b: 
        sum += x**2
        x += 1
    return sum



a, b = map(int, input().split())
print(square_sum(a, b))
