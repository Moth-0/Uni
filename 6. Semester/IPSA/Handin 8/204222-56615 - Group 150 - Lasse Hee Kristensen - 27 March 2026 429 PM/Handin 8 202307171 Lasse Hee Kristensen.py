#%%
'''
Vi starter med at indføre "memoize" funktionen fra forelæsningen,
som gemmer tidligere resultater fra recursion calls for at spare
tid. Vi bruger den som decorator på begge funktioner.

Til a) nedskriver vi vores 3 forskellige cases. Base case
er at en af strengene er tomme og subsequence må have længde 0.
Ellers hvis sidste bogstav er det samme, må vi fjerne det og 
tilføje 1 til længden af resultatet. Ellers har vi to forskellige
bogstaver og må undersøge hvilken af dem resulterer i den 
længste subsequence med max() funktionen.

Til b) bruger vi præcis samme cases men indser at vi skal returne
en string hvor vi appender x[-1] hvis x[-1]==y[-1], og elelrs
har base case der returnerer en tom string eller at 
vi bliver nødt til at kigge på den substring der giver længste
LCS for at komme videre. lcs_length bruges derfor igen.


'''
#a)
def memoize(f): #Dynamic programming funktion, der husker funktionskalds resultater
# answers[args] = f(*args)
    answers = {}
    def wrapper(*args):
        if args not in answers:
            answers[args] = f(*args)
        return answers[args]
    return wrapper

@memoize
def lcs_length(x, y):
    '''finder længden af den længste common subsequence mellm x og y'''
    if x == "" or y == "": #lcs giver '' hvis en af strengene er tom
        result = 0
    elif x[-1] == y[-1]:
        result = lcs_length(x[:-1], y[:-1]) + 1
    elif x[-1] != y[-1]:
        result = max(lcs_length(x[:-1], y), lcs_length(x, y[:-1]))
    return result

#b)
@memoize
def lcs(x, y):
    if x == "" or y == "": #lcs giver '' hvis en af strengene er tom
        result = ""
    elif x[-1] == y[-1]:
        result = lcs(x[:-1], y[:-1]) + x[-1]
    elif lcs_length(x[:-1], y) > lcs_length(x, y[:-1]):
        result = lcs(x[:-1], y) #returner den længste string af de to mulige   
    else:
        result = lcs(x, y[:-1])
    return result
    
L1 = 'abca'
L2 = 'acba'
L3 = '**a**z**ra**el'
L4 = '**a**bracadab**ra**'

print(f"Den lænsgte subsequence af {L3} og {L4} er", lcs(L3, L4)
      , "og har længde", lcs_length(L3, L4))



# %%
