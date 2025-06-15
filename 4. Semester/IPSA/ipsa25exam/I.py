'''
    FORBIDDEN

    Create a decorator @forbidden(value1, value2, ..., default=<default>) that
    takes a sequence of 1 to 1000 hashable values, and decorates a function 
    that can take an arbitrary number of positional and keyword arguments, such 
    that if the function was to return one of the listed values, it instead 
    returns the value <default> (if the 'default' keyword argument is omitted, 
    the default return value is None).

    Input: Multiple lines of Python code using the decorator forbidden. 
           The last line contains the string '#eof'.

    Output: The result of executing the Python code.

    Example:

      Input: @forbidden(4, 25)
             def square(n):
                 return n ** 2
             
             for n in range(10):
                 print(n, square(n))
             #eof

      Ouput: 0 0
             1 1
             2 None
             3 9
             4 16
             5 None
             6 36
             7 49
             8 64
             9 81

    Note: The below code already takes care of reading the input and evaluating
          it. Your task is only to create the decorator forbidden.
'''


# insert code
def forbidden(*args, default=None, **kwargs): 
    def decorator(f): 
        def wrapper(*x): 
            out = f(*x)
            if out in args or kwargs: 
                return default
            else: 
                return out
        return wrapper
    return decorator



import sys
code = ''
for line in sys.stdin:
    if line.startswith('#eof'):
        break
    code += line
exec(code)