"""
202408911 Safiya Chebil
202406237 Marie Schnoor-Madsen
202407458 Kenny Nguyen
"""

from string import ascii_letters, digits
s = open('saxo.txt', encoding='utf8').read()
s = s.lower()
s = ''.join([c for c in s if c in ascii_letters or c in digits])
len(s)


listy =[]
for i in range(1,len(s)):
    h = i 
    v = i 
    while v >= 0 and h < len(s) and s[v] == s[h]: #for lige palindromes
        if h - v + 1 >= 7: #sikre at minimum længde er 7
            x = s[v:h+1] 
            listy.append(x)

        h += 1
        v -= 1 

    h = i + 1 
    v = i
    while v >= 0 and h < len(s) and s[v] == s[h]: #for ulige palindromes 
        if h - v + 1 >= 7:
            x = s[v:h+1] 
            listy.append(x) 

        h += 1 
        v -= 1
print(len(listy))

#overvejselser: brug af while loop i stedet for for loop, da det er hurtigere
#koden chekker for alle indekse udenfor i og kun appender når betingelsen er opfyldt(lengden af sækvensen er mere end 7)
#koden er delt op i to while loops, som tager højde for om længden af palindromet er ulige eller lige. 
#vi havde det sværest med at bruge slicing rigtigt