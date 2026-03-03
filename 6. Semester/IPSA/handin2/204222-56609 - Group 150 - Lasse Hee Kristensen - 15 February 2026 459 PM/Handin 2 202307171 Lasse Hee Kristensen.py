#Exercise 4.13 - handin 2 (palindrome)

'''
HANDIN 2 (palindromes)

This handin is done by (study ids and names of up to three students):

    202307171 Lasse Hee Kristensen

Reflection upon solution:
Jeg startede med at forsøge at løse det hele med en stor for løkke, men indså det blev for kompliceret,
hvis jeg både skulle finde de lige og ulige palindromer. Derfor prøvede jeg i stedet
at lave en kode, der først tjekker 'symmetrisk' rundt om et bogstav, og bagefter et, der er 
næsten magen til, men som sammenligner med bogstavet lige til højre for - dvs. i og i+1 i stedet for

Koden itererer altså over hvert eneste bogstav i den string, vi henter fra teksten, og tjekker
bogstavet umiddelbart til højre for og bogstaverne rundt om, for at se om det er muligt at danne
et palindrom. While-loopet sørge for at prøve at udvide palindromet, for at få det størst mulige,
men appender det til en liste af palindromer hver gang den finder et nyt match med længde større 
eller lig 7. Det er sikkert muligt at komprimere koden, men jeg synes den er blevet overskuelig nu.
(I while-loppsne er også et sikkerhedstjek for at undgå out-of-bounds fejl, når vi leder)

'''


from string import ascii_letters, digits
s = open(r'saxo.txt', encoding='utf8').read()
s = s.lower()
s = ''.join([c for c in s if c in ascii_letters or c in digits])

palindromes = []

for i in range(len(s)-1):
    #vi tjekker palindromer med centrum i 'i'
    j = 0
    while i - j >= 0 and i + j <= len(s) and s[i-j]==s[i+j]:
            palindrome = s[i-j:i+j+1] #når vi slicer skal vi huske at endepunkt ekskluderes, så +1
            if len(palindrome) >= 7: #hvis længden af palindromet er 7 eller mere, skal det med
                  palindromes.append(palindrome)
            j += 1 #vi tjekker om palindromet kan udvides ved at incremente j
    
    #vi tjekker palindromer med centrum mellem i og i+1
    j = 0

    while i - j >= 0 and i + j <= len(s) and s[i-j]==s[i+j+1]:
            palindrome = s[i-j:(i+j+1)+1] #når vi slicer skal vi huske at endepunkt ekskluderes, så +1
            if len(palindrome) >= 7: #hvis længden af palindromet er 7 eller mere, skal det med
                  palindromes.append(palindrome)
            j += 1 #vi tjekker om palindromet kan udvides 

print("Palindromerne er: ", palindromes)
print("Antal palindromer fundet: ", len(palindromes))