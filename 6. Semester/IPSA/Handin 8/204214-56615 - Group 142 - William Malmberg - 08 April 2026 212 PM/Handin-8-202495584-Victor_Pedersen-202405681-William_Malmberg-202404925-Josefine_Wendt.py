'''
HANDIN 8 (Longest common subsequence)

This handin is done by (study ids and names of up to three students):

    202405584 Victor Kvist Loft Pedersen
    202405681 William Malmberg
    202404925 Josefine Ella Luci Sandy Dorothea Wendt

    Reflections upon solutions
    This handin was all about being able to implement the three basic observations
    given in the the description.
    We had to figure out how we can implement the recursion function and how we
    can use @cache to shorten the runtime, and make the program less intensive. T
    his assignment gave us a good understanding of decoraters and recursion.
'''

from functools import cache
def lcs_length(x:str, y:str) -> int:
    assert isinstance(x, str)
    assert isinstance(y, str)
    
    @cache
    def solve(x, y) -> int:
        if x == "" or y == "":
            return 0
        if x[-1] == y[-1]:
            return solve(x[:-1], y[:-1]) + 1
        else:
            return max(solve(x[:-1], y), solve(x, y[:-1]))
        
    return solve(x, y)

def lcs(x:str,y:str) -> str:
    assert isinstance(x, str)
    assert isinstance(y, str)
    
    @cache
    def solve(x, y) -> str:
        if x == "" or y == "":
            return ""
        if x[-1] == y[-1]:
            return solve(x[:-1], y[:-1]) + x[-1]
        else:
            return max(solve(x[:-1], y), solve(x, y[:-1]), key=len)
        
    assert len(solve(x, y)) == lcs_length(x, y), "Not correct solution"
    return solve(x, y)

x = "abracadabrae"
y = "azrael"

subseq = lcs(x, y)
length = lcs_length(x, y)

print("LCS:", subseq)
print("Length:", length)