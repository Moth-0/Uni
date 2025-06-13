'''
    3-DISTINCT

    Given a string, print all distinct substrings containing exactly 
    3 distinct letters. For example, the string SUMMER has 5 such
    substrings: MER, MMER, SUM, SUMM, and UMME (in alphabetic order).

    Input:  A singe line with a string of length at most 100 and 
            only containing letters A-Z.

    Ouput:  All distinct substrings containing exactly 3 distinct letters,
            sorted in alphabetic order with one substring per line.

    Example:

      Input:  SUMMER

      Output: MER
              MMER
              SUM
              SUMM
              UMME
'''


# insert code
text = input()
n = len(text)

substrings = set()

for i in range(n): 
    for j in range(i+1, n+1): 
        substr = text[i:j]
        if len(set(substr)) == 3: 
            substrings.add(substr)
    
for t in sorted(substrings):
    print(t)
