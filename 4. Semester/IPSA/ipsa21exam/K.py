'''
    NONNEGATIVE

    Your task is to create a decorator 'nonnegative', that should
    take a function f and return a new function that returns f(x),
    if f(x) >= 0, and otherwise returns zero.

    If we apply the decorator nonnegative as 

        @nonnegative
        def cubed(x):
            return x ** 3

    then cubed(4) = 64 and cubed(-2) = 0.

    Input:  Two lines. The first line is a Python expression 
            using the decorator nonnegative, to create a function f.
            The second line is a Python list L of integers, where
            1 <= len(L) <= 100.

    Output: One line for each integer x in L, containing x and f(x), 
            separated by space. The result f(x) should be printed 
            with 3 decimals.

    Note: 

      The below code already handles the input and ouput. 
      Your task is only to create the decorator nonnegative.
'''


def nonnegative(f):
    # insert code

    pass



nonnegative_function = eval(input())
L = eval(input())

for x in L:
    y = nonnegative_function(x)
    print(x, f'{y:.3f}')
