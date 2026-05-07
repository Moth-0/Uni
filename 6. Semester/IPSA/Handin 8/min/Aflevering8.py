"""
HANDIN 8 - longest common subsequence

This handin is done by: 
    202307989 Mikkel Moth Billing 

Reflection upon solution: 
    I found it easier to find the string first by just following the steps in the excersise, i then rewrote it to find a length afterwards. 
    I testet that memoize works by putting in some long strings and running it with and without, it is a lot faster with :). 
"""

# memoize function form lectures
def memoize(f):
    answers = {}
    def wrapper(*args):
        if args not in answers:
            answers[args] = f(*args)
        return answers[args]
    return wrapper


# Use memoize and go through the strings with the algoritm from the exercise description.
# Then it takes the max value of all the solution found.
@memoize
def lcs_length(x, y): 
    if x == '' or y == '': 
        return 0
    elif x[-1] == y[-1]: 
        return lcs_length(x[:-1], y[:-1]) + 1
    else:
        return max([lcs_length(x[:-1], y), lcs_length(x, y[:-1])])
    

print(lcs_length('abra', 'azrael'))


# Again go through the strings, instead of adding a 1 we add the letter to a string. 
# Then take the longest string of all found solutions.
@memoize
def lcs(x,y): 
    if x == '' or y == '': 
        return ''
    elif x[-1] == y[-1]: 
        return lcs(x[:-1], y[:-1]) + x[-1]
    else:
        return max([lcs(x[:-1], y), lcs(x, y[:-1])], key=len)
    

def trace(f): # decorator to trace recursive calls
    indent = 0
    def wrapper(*args):
        nonlocal indent
        spaces = '| ' * indent
        arg_str = ', '.join(map(repr, args))
        print(spaces + f'{f.__name__}({arg_str})')
        indent += 1
        result = f(*args)
        indent -= 1
        print(spaces + f'> {result}')
        return result
    return wrapper

@trace
#@memoize
def lcs(x,y):
    
    if x == '' or y == '':
        pass
    elif x[-1] == y[-1]:
        sub += (lcs(x[:-1], y[:-1]) + x[-1])
    else: 
        for run in [lcs(x[:-1], y), lcs(x, y[:-1])]:
            sub += run
    
    return sub
    
print(lcs('1234', '1324'))