'''
Handin 2
This is done by :
748507 Kristian Milla

Reflection upon solution:
Koden tjekker hvert bogstav i strengen, hvor den kigger på naboen på hver side.
Hvis naboerne er ens, kigger den på næste sekvens af naboer.
Hvis 3 sæt naboer eller mere er ens, appender den sekvens til vores palindromics
Men! Dette antager at bogstavet er i midten af sekvensen. Det vil sige sekvensen har ulige længde.
Derfor er der lavet en ekstra kode der tjekker lige palindromer.
Den bruger en usymmetrisk indeksering når vi skal tjekke naboer.
Det svarer til at du definerer midten af sekvensen mellem 2 bogstaver.
'''

from string import ascii_letters, digits
s = open('saxo.txt', encoding='utf8').read()
s = s.lower()
s = ''.join([c for c in s if c in ascii_letters or c in digits])

p_odd = []
p_even = []

for i in range(len(s)-1):
    j = 1
    while i-j >= 0 and i+j < len(s):
        while s[i-j]==s[i+j]:
            if j>=3:
                p_odd.append(s[i-j:i+j+1])
            j = j+1
        else:
            break

for i in range(len(s)-1):
    j = 0
    while i-j >= 0 and i+j < len(s):
        while s[i-j]==s[i+(j+1)]:
            if j>=3:
                p_even.append(s[i-j:i+j+2])
            j = j+1
        else:
            break

print('palindromics with odd length and >= 7', p_odd)
print('no of palindromics with odd length', len(p_odd))
print('palindromics with even length and >= 7', p_even)
print('no of palindromics with even length', len(p_even))
