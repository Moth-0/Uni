"""
HANDIN 8 (Longest common subsequence)

This handin is done by:
    202405797 Johannes Bøgh Fangel
    202407470 Valdemar Scheel

Reflection upon solution:
    It was rather difficult to make a recursive function, but using trace helped see the different parts happening.
    At first, we found it difficult to properly structure the function and get the right returns.
    We also had a bit of struggle getting the memoize to work properly as we had to ensure that each input was not a unique input.
    Otherwise, we mainly followed the 'recipe' provided to make it work.
    
"""


def trace(f):  # decorator to trace recursive calls
    indent = 0
    def wrapper(*args):
        nonlocal indent
        spaces = '|  ' * indent 
        arg_str = ', '.join(map(repr, args))
        print(spaces + f'{f.__name__}({arg_str})')
        indent += 1
        result = f(*args)
        indent -= 1
        print(spaces + f'> {result}')
        return result
    return wrapper
def memoize(f):
    answers = {}
    def wrapper(*args):
        if args not in answers:
            answers[args] = f(*args)
        return answers[args]
    wrapper.__name__ = f.__name__ + '_memoize'
    return wrapper


x, y = '**a**bracadab**ra**', '**a**z**ra**el'

def LCS(x,y):
    @memoize
    def lcs(x,y):
        if x == '' or y == '':
            return ''

        elif x[-1] == y[-1]:

            return lcs(x[:-1],y[:-1])+x[-1]
  
        elif x[-1] != y[-1]:

            return max(lcs(x[:-1],y),lcs(x,y[:-1]),key=len)
    
    def lcs_len(lst):
        return len(lst)

    Longest_commom_subsequence = lcs(x,y)

    return f"The longes common subsequence is {Longest_commom_subsequence} with a length of {lcs_len(Longest_commom_subsequence)}"


LCS(x,y)
