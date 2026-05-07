'''
HANDIN 8 (longest common subsequence)

This handin is done by:

    202106248 Matilde E. Hansen
    202105331 Elias R. Skjoldborg

Reflection upon solution: 

There were no major problems in the solving of this handin, as the needed algorithem was explained in detail in the problem text.
The two functions are nearly identical, the only difference being that one returns the lenght of a solution string and the other returns the actual string.
The longest common subsequence is not always unique, and this solution will only return one possible answer, should multiple exist.

'''


def memoize(f):                         # Since we often want to use the same function with the same input, we take advantage of the memoize wrapper
    answers= {}
    def wrapper(*args):
        if args not in answers:
            answers[args] = f(*args)
        return answers[args]
    return wrapper

@memoize
def lcs_length(x, y):           # We use recursion to solve this problem
    if x == '' or y == '':      # Base case is then that x or y is empty, which would make the longest common subsequence 0
        return 0
    elif x[-1] == y[-1]:
        return 1 + lcs_length(x[:-1], y[:-1])   #If the last element of x and y are identical, the solution is equal to 
                                                # 1 + the solution to the problem if we removed that last element of x and y
    else:
        return max(lcs_length(x[:-1], y), lcs_length(x, y[:-1])) 
    #If the last element of x and y aren't equal, then we try two possible smaller permutations of the input, and return wichever is greater.
    #This will also try every possible combination of x and y


@memoize
def LCS(x,y):                   # To find the longest substring explicitly, we do the same as in the lcs_length function, but return the strings instead of their length
    if x == '' or y == '':
        return ''
    elif x[-1] == y[-1]:
        return LCS(x[:-1], y[:-1]) + x[-1]
    else:
        return max(LCS(x, y[:-1]), LCS(x[:-1], y), key = len)
    
print(LCS('**a**bracadab**ra**', '**a**z**ra**el'))
print(LCS('abca', 'acba'))