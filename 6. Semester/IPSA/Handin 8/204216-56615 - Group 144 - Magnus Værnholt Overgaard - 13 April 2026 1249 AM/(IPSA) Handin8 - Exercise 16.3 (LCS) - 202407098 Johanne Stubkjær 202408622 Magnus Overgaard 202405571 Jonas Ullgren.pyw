"""
HANDIN 8 - Exercise 16.3 (longest common subsequence)

This handin is done by:

202407098 Johanne Stubkjær
202408622 Magnus Overgaard
202405571 Jonas Ullgren

Reflection upon solution:

Our solution uses recursion and follows the core idea as explained in the exercise - If one of the strings is empty then the 
only possible LCS is the empty string '' with length 0. If the last characters match we add 1 to the length, and that character 
can be added onto the end of the LCS-string. If they do not match the code tries two paths by removing the last character from 
one string at a time. It then compares the two different paths/results to find the longer solution.
To make the code run fast we use the memoize decorator that Gerth has shown us, which makes the function "store" previous 
computations instead of having to run the same things over and over.
"""

# memoize function made by Gerth
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


# Part (a) - Computes length of LCS
@memoize
def lcs_length(x, y):
    if not x or not y:    # Base case explained in the exercise
        return 0          # If one string is empty --> no LCS
        
    if x[-1] == y[-1]:    # If last characters match --> contributes 1 to LCS length
        return 1 + lcs_length(x[:-1], y[:-1])
        
    else:                 # otherwise try removing last character from each string and keep larger result
        return max(lcs_length(x, y[:-1]), 
                   lcs_length(x[:-1], y))


# Part (b) - Computes an actual LCS
@memoize
def lcs(x,y, subseq_so_far = ''):
    if not x or not y:    # If one string empy --> return the subsequence built so far
        return subseq_so_far
        
    # If last characters match --> include in the result
    # We work backwards through string, so add character to the front of subsequence built so far
    if x[-1] == y[-1]:    
        return lcs(x[:-1],
                   y[:-1], 
                   x[-1] + subseq_so_far)

    else:                 # Otherwise Try removing last chracter of second string, and then first string
        path_1 = lcs(x, y[:-1], subseq_so_far)
        path_2 = lcs(x[:-1], y, subseq_so_far)

    # Returns the longer one of the subsequence paths
    return path_1 if len(path_1) > len(path_2) else path_2


# Combined function
def analyze_lcs(string_1, string_2):
    length = lcs_length(string_1, string_2)
    subsequence = lcs(string_1, string_2)
    print(f"Length of a longest common subsequence:   {length}")
    print(f"One longest common subsequence is:        {subsequence}")


# Example
test_string1 = 'dfewqfqwfrqsafeaierniuovndf'
test_string2 = 'bojfewfwqfwqfevgenbefovbhnfshopiwwkbmpeidff'

analyze_lcs(test_string1, test_string2)