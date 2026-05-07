'''
HANDIN 8 (longest common subsequence)

This handin is done by (study ids and names of up to three students):

    202406267 Andreas Wind

Reflection upon solution:

    Først var jeg forvirret over hvorfor man først skulle lave funktionen
    med længden og så den rigtige lcs, men som jeg lavede det gav det
    mening, da det var meget nemmere at forstå logikken i problemet når
    det bare handler om længder, og så var det nemt at lave det om til 
    at finde den faktiske string frem for bare længden. Og så skulle man
    selvfølgelig også bruge lcs_length i lcs funktionen. Rekursion giver
    mere og mere mening for mig.
    
    
    
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
    
    # base case
    if x == '' or y == '':
        return 0
    
    if x[-1] == y[-1]:
        return int(lcs_length(x[:-1], y[:-1])) + 1
    
    if x[-1] != y[-1]:
        return max(lcs_length(x[:-1], y), lcs_length(x, y[:-1]))

        
print(lcs_length('**a**bracadab**ra**', '**a**z**ra**el'))


@memoize
def lcs(x,y):

    if x == '' or y == '':
        return ''
    
    if x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1]
    
    if x[-1] != y[-1]:
        if lcs_length(x[:-1], y) >= lcs_length(x, y[:-1]):
            return lcs(x[:-1], y)
        else:
            return lcs(x, y[:-1])

print(lcs('**a**bracadab**ra**', '**a**z**ra**el'))
