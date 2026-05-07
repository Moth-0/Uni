'''
HANDIN 8 (longest common subsequence)

This handin is done by:
    202308053 Nanna Bank-Pedersen

Reflection upon solution:
Jeg synes opgaven var lidt svær at forstå i starten, især hvordan den rekursive 
løsning skulle fungere og hvorfor man skal vælge mellem to muligheder når 
tegnene ikke matcher.
Jeg havde også lidt udfordringer med memoization, da jeg først ikke fik det 
implementeret korrekt.
Min løsning består af to funktioner: en der finder længden af den længste fælles 
subsequence, og en der finder selve subsequencen. Jeg bruger rekursion og 
sammenligner de sidste tegn i strengene for at bygge løsningen op. Jeg antager at 
input er gyldige strenge og har ikke lavet ekstra fejlhåndtering.
'''

def memoize(func):
    cache = {}

    def wrapper(x, y):
        if (x, y) not in cache:
            cache[(x, y)] = func(x,y)
        return cache[(x, y)]
        
    return wrapper

@memoize
def lcs_lenght(x, y):
    if x == '' or y == '':
        return 0
    
    if x[-1] == y[-1]:
        return 1 + lcs_lenght(x[:-1], y[:-1])
    
    return max(
        lcs_lenght(x[:-1], y),
        lcs_lenght(x, y[:-1])
    )

@memoize
def lcs(x, y):
    if x == '' or y == '':
        return ''
    
    if x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1]
    
    if lcs_lenght(x[:-1], y) >= lcs_lenght(x, y[:-1]):
        return lcs(x[:-1], y)
    else:
        return lcs(x, y[:-1])


x = "abracadabrae"
y = "azrael"

subseq = lcs(x, y)
length = lcs_lenght(x, y)

print("LCS:", subseq)
print("Length:", length)