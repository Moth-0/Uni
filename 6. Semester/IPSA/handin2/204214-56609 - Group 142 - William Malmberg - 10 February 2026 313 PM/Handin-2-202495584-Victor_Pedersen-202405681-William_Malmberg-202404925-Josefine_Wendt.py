'''
HANDIN 2 (Palindromes)

This handin is done by (study ids and names of up to three students):

    202405584 Victor Kvist Loft Pedersen
    202405681 William Malmberg
    202404925 Josefine Ella Luci Sandy Dorothea Wendt

Reflection upon solution:

    We first discussed how to quickly discard non palidromes. After that we had some issues with which method was
    the fastest to identify the correct palindromes from seven and above. Therefore we endeded up with a method where,
    we start in the center and expand outwards in the word. We also had to divide between even and odd words, since they
    have different centers. Then the last part of the issue was just to make the numbers match for even and odd words,
    when the words where looked through.
'''

def find_palindromes(text):
    palindrome = []

    for i in range(1, len(text)-1):
        if text[i] == text[i+1]: # Tjekker for lige palindromer
            for j in range(0, min(i+1, len(text)-(i+1))):

                if text[i-j] == text[i+1+j]:
                    if len(text[i-j:i+1+j]) >= 7:
                        palindrome.append(text[i-j:i+1+j])
                else:
                    break

        else: # Tjekker ulige palindromer
            for j in range(1, min(i+1, len(text)-i)):
                
                if text[i-j] == text[i+j]:
                    if len(text[i-j:i+1+j]) >= 7:
                        palindrome.append(text[i-j:i+1+j])
                else:
                    break

    print(len(palindrome))

from string import ascii_letters, digits
s = open(r'tests\saxo.txt', encoding='utf8').read()
s = s.lower()
s = ''.join([c for c in s if c in ascii_letters or c in digits])*10

find_palindromes(s)