'''
    DENSE SAMPLE

    Given a list of positive weights, the task is to find a subsequence (sample)
    of the weights such that 1) the subsequence has minimum sum, 2) among every
    three consecutive weights in the lists, at least one of them is in the 
    sample. It is guaranteed that there is a unique minimum weight solution.

    Input:  A single Python list L of integers (weights), where 
            3 <= len(L) <= 100 and all elements are between 1 and 1000.

    Output: A single line with a Python list of strictly increasing indexes 
            into L defining a sample, where the weights in the sample have
            minimum sum, and among every three consecutive indexes into L, 
            at least one is in the sample.

    Example:

      Input:  [7, 5, 7, 5, 7, 6, 7]

      Output: [1, 4]

      Explanation: In the input list L, L[1] + L[4] = 5 + 7 = 12 achieves the 
      minimum possible weight sum, if for all three consecutive indexes at least 
      one index is in the sample.
    
    Note: The below code already reads the input list L.
'''

# What is this asking????
# Im not sure of the logic so the answer is flawed 
L = eval(input())
# insert code

i = 0 
out = []

def solve(i, L): 
    if len(L) == 5: 
        out.append((i+2))
    elif len(L) == 4:
        l = [L[2], L[1]]
        j = 2-l.index(min(l))
        out.append((i+j))
    elif len(L) == 3: 
        l = [L[2], L[1], L[0]]
        j = 2-l.index(min(l))
        out.append((i+j))
    elif len(L) >= 6: 
        l = [L[2], L[1], L[0]]
        j = 2-l.index(min(l))
        out.append((i+j))
        solve((i+j+1), L[j+1:])
    
        
solve(i, L)
print(out)