'''''
This is done by :
748507 Kristian Milla

Reflection upon solution:
Når man sætter koden in i Pythontutor går det op for en hvor mange ens
computationer koden skal igennem, og hvorfor det således giver mening 
med cache decorator.
Synes det var nemmere faktisk at regne opgave b, fordi den virker mindre
abstrakt og det er lettere at forstå formålet (men måske jeg er farvet af
jeg regnede opgave a først).
Synes logikken i hvad en subsequence egentlig er og at de ikke behøver være
sammenhængende var forvirrende, og accepterede bare lidt Gerts "opskrift".
'''

import functools

@functools.cache
def lcs_length(x, y):
    # Basistilfælde: Hvis en af strengene er tomme, er fælleslængden 0
    if not x or not y:
        return 0
    
    # Hvis de sidste tegn matcher
    if x[-1] == y[-1]:
        return 1 + lcs_length(x[:-1], y[:-1])
    
    # Hvis de ikke matcher, prøv begge veje og tag den største (max)
    else:
        return max(lcs_length(x[:-1], y), lcs_length(x, y[:-1]))
    

import functools

@functools.cache
def lcs(x, y):
    # Basistilfælde: Hvis en af strengene er tomme, er den fælles streng tom
    if not x or not y:
        return ""
    
    # Hvis de sidste tegn matcher
    if x[-1] == y[-1]:
        # Tag resultatet fra resten og klistr det fælles tegn bagpå
        return lcs(x[:-1], y[:-1]) + x[-1]
    
    # Hvis de ikke matcher
    else:
        res1 = lcs(x[:-1], y)
        res2 = lcs(x, y[:-1])
        
        # Returnér den længste af de to strenge
        if len(res1) >= len(res2):
            return res1
        else:
            return res2

print(lcs('abracadabra', 'azrael')) 