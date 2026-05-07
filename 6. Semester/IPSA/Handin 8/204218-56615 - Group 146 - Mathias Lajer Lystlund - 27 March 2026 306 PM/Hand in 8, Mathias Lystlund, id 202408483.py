'''
HANDIN 8 (Longest common subsequence)

This handin is done by Mathias Lystlund, id: 202408483:

  

Reflection upon solution:

I approached the LCS problem by first building a recursive solution that actually constructs the subsequence, 
by using the 'if-statements' given in the problem description, which helped me understand the structure more deeply.
Then i realized that i could approach the 'lcs_length' problem as i did in Exercise 16.1, b).
One challenge was realizing that max() on strings does not compare lengths, but lexicographical order, 
which led to incorrect results. 
'''





def memoize(f):
    # answers[args] = f(*args)
    answers = {}
    def wrapper(*args):
        if args not in answers:
            answers[args] = f(*args)
        return answers[args]
    return wrapper



@memoize
def lcs_length(x, y):
    if x == '' or y == '':
        return 0
 
    
    if x != '' and y != '' and x[-1] == y[-1]:
        return 1 + lcs_length(x[:-1], y[:-1])
       
    if x != '' and y != '' and x[-1] != y[-1]:
        return max(lcs_length(x[:-1], y), lcs_length(x, y[:-1]))
    
   

print(lcs_length('absdeks', 'adsdkes'))


@memoize
def lcs(x, y):
    if x == '' or y == '':
        return ''
 
    
    if x != '' and y != '' and x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1]
        
        
    if x != '' and y != '' and x[-1] != y[-1]:
        return max(lcs(x[:-1], y), lcs(x, y[:-1]), key=len)
    
 

print(lcs('absdeks', 'adsdkes'))