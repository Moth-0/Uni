#%%
#Exercise 16.3 - handin 8 (longest common subsequence)


'''
HANDIN 8 (Handin 8 - longest common subsequence)

This handin is done by 
    202305360: Arunchand Suriyakumar

Reflection upon solution:
    We directly use the cases provided in the task to create the recursive function.
    We only notice to change x[-1] to "1" in the lcs_lenght function. 
    To make sure, we get the longest common subsequence, we have to find the max
    (defined by the lenght of the sequence) of the two possible directions. 
    Otherwise both functions are near identical.
'''

#%%
def memoized(f):
    answers = {}
    def wrapper(*args):
        if args not in answers:
            answers[args] = f(*args)
        return answers[args]
    return wrapper


@memoized
def lcs_lenght(x ,y):
    if x == '' or y == '':
        return 0
    elif x != '' and y != '' and x[-1] == y[-1]:
        return lcs_lenght(x[:-1], y[:-1]) + 1
    elif x != '' and y != '' and x[-1] != y[-1]:
        return max(lcs_lenght(x[:-1], y), lcs_lenght(x, y[:-1]))
    

lcs_lenght('abca', 'acba')

#%%
@memoized
def lcs(x ,y):
    if x == '' or y == '':
        return ''
    elif x != '' and y != '' and x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1]
    elif x != '' and y != '' and x[-1] != y[-1]:
        return max(lcs(x, y[:-1]), lcs(x[:-1], y), key = len)
    

lcs('**a**bracadab**ra**', '**a**z**ra**el')