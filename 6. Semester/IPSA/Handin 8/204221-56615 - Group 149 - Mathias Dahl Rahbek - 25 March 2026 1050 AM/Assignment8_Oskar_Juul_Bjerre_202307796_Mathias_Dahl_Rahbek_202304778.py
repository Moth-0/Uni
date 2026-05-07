'''
HANDIN 8 (longest common subsequence)

202307796 Oskar Juul Bjerre
202304778 Mathias Dahl Rahbek

Reflection upon solution:
Easy peasy lemon squeezy. We wrote this code in 20 minutes. We wrote the lcs function based on the lcs_length function, changing all the int operators to string operators. 
'''
from functools import cache

@cache
def lcs_length(x, y):

    if x == '' or y == '': # Basecase
        return 0

    if x[-1] == y[-1]:
        return lcs_length(x[:-1], y[:-1]) + 1
    
    return max(lcs_length(x[:-1], y), lcs_length(x, y[:-1]))

@cache
def lcs(x, y):

    if x == '' or y == '': # Basecase with str
        return ''

    if x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1]
        
    if len(lcs(x, y[:-1])) <= len(lcs(x[:-1], y)): # Check longest subsequence
        return lcs(x[:-1], y)

    return lcs(x, y[:-1])
