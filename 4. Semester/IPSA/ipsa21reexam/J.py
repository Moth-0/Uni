'''
    SQUEEZE

    Your task is to create a decorator @squeeze(low, high), that 
    takes two numbers low <= high as arguments, and when applied
    to a function f returns a new function that returns f(x) if
    low <= f(x) <= high, returns low if f(x) < low, and returns
    high if f(x) > high.

    If we apply the decorator squeeze as 

        @squeeze(-50, 10)
        def f(x):
            return x ** 3

    then f(2) = 8, f(3) = 10 (since 3 ** 3 = 27 > 10), f(-3) = -27,
    and f(-4) = -50 (since (-4) ** 3 = -64 < -50).

    Input:  Two lines. The first line is a Python expression 
            using the decorator squeeze, to create a function f.
            The second line is a Python list L of numbers, where
            1 <= len(L) <= 100.

    Output: One line for each x in L, containing x and f(x),
            separated by space. The result f(x) should be printed
            with 3 decimals.

    Example:

      Input:  squeeze(-50, 10)(lambda x: x ** 3)
              [-4, -3, -2, -1, 0, 1, 2, 3, 4]

      Output: -4 -50.000
              -3 -27.000
              -2 -8.000
              -1 -1.000
              0 0.000
              1 1.000
              2 8.000
              3 10.000
              4 10.000

    Note: 

      The below code already handles the input and ouput. 
      Your task is only to create the decorator squeeze.
'''


def squeeze(low, high):
    # insert code
    def decorator(f):
        def wrapper(x): 
            if f(x) < low: 
                return low
            elif f(x) > high: 
                return high
            else:
                return f(x)
        return wrapper
    return decorator



squeezed_function = eval(input())
L = eval(input())

for x in L:
    result = squeezed_function(x)
    print(x, f'{result:.3f}')
