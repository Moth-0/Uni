# -*- coding: utf-8 -*-
"""

    HANDIN 2 (Palindrome)

This handin is done by (study ids and names of up to three students):

    202406267 Andreas Wind

Reflection upon solution:

    først havde jeg problemer med palindromer med lige antal bogstaver fordi
    jeg bruger midterbogstavet til noget i programmet. Men så fandt jeg ud af 
    at jeg bare skulle indeksere lidt anderledes med lige bogstaver.
    Så lavede jeg først et tjek om der var lige bogstaver eller ej, og så havde
    jeg to forskellige, men næsten identiske loops: 1 for ulige og 1 for lige.
    Den akavede løsning fiksede jeg ved at lave en variabel d som er 1 hvis der
    er ulige antal bogstaver og 0 ellers.
"""


from string import ascii_letters, digits
s = open('saxo.txt', encoding='utf8').read()
s = s.lower()
s = ''.join([c for c in s if c in ascii_letters or c in digits])


for j in range(7,11):
    j_list = []
    j_antal = 0
    if j % 2 != 0: # ulige antal bogstaver
        # d står for displacement og er den forskydning som skal ske hvis
        # der arbejdes med ulige tal. Den er 1 hvis ulige og 0 hvis lige
        d = 1
    else: # lige antal bogstaver
        d = 0
        
    for i in range(len(s)):
    # antag at i er midten af et palindrom. hvis der er "symmetriske"
    # bogstaver i mindst 3 bogstaver ude så er det et palindrom af længde
    # mindst 7
        #kig på j til hver side og se om der er symmetri:
        half = (j-d)//2
        right = s[d+i:i+half+d]
        right_reverse = right[::-1]
        if s[i-half:i] == right_reverse:
            word = s[i-half:i+half+1]
            if word not in j_list:
                j_list.append(word)
            j_antal += 1
    #print(j_list)
    if j_antal != 0:
        print(j_antal, "palindromes with length", j)
        print("(",len(j_list), "distinct )")
