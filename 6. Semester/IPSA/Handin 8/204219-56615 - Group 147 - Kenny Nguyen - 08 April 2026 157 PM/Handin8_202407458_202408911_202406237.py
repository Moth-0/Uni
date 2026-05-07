'''
HANDIN 8 (longest comment subsequence)

This handin is done by (study ids and names of up to three students):

    202407458 Kenny Nguyen
    202408911 Safiya Chebil 
    202406237 Marie Schnoor - Madsen 

    
Reflection upon solution:

    Det store problem i denne aflevering, var selve forståelsen af opgaven. Hvad de to forskellige funktioner skulle gøre, især funktion fra b)
    hvad den specifik skulle gøre. Der var tvivl omkring hvorvidt funktion skulle tage hensyn til at det ikke var en unik løsning men der var flere.
    Om at vi skulle printe alle de mulige subsequences der var. 
'''

#a)
def memoize(f):
# answers[args] = f(*args)
    answers = {}
    def wrapper(*args):
        if args not in answers:
            answers[args] = f(*args)
        return answers[args]
    return wrapper 

@memoize
def LCS_length(x, y): 
    if x == '' or y == '': 
        return 0 
    if x[-1] == y[-1]: 
        k = LCS_length(x[:-1], y[:-1]) + 1
        return k
    else:
        return max(LCS_length(x[:-1], y), LCS_length(x, y[:-1]))

LCS_length('**a**bracadab**ra**', '**a**z**ra**el')

@memoize
def LCS(x,y):
    if x=="" or y=="":
        return ""
    if x[-1]==y[-1]:
            return LCS(x[:-1],y[:-1])+x[-1]
    else:
        ene_side=LCS(x[:-1],y)
        anden_side=LCS(x,y[:-1])
        return ene_side if len(ene_side)>len(anden_side) else anden_side 
        

LCS('**a**bracadab**ra**', '**a**z**ra**el')

