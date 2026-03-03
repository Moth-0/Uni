#Exercise 4.13 - handin 2 (palindrome)
'''
HANDIN 2 (Down payment)

This handin is done by 
    202305360: Arunchand Suriyakumar

Reflection upon solution:
    The idea is to find the palindromes by looking at one letter and compare the surronding letters. The result then depends on whether the we look at even
    or odd palindromes. In the case of odd palindromes, we can for a given letter look at its surrounding letters and if they are equal, we have found a palindrome.
    We continue to the next surrounding letter until this is not satisfied. Similarly, for the even palindromes, we first compare the given letter with the letter beside 
    it and do the same thing as for the odd case. We ensure checking that we are not going outside the text. This is done using a while-condition. The approaite
    slicing are then used to draw the palindromes out of the text into a list. 
'''



from string import ascii_letters, digits
s = open('saxo.txt', encoding='utf8').read()
s = s.lower()
s = ''.join([c for c in s if c in ascii_letters or c in digits])

palindromes_odd = []
palindromes_even = []



#Odd palindromes
for i in range(len(s)):
    j = 1
    while i-j >= 0 and i+j < len(s) and s[i-j] == s[i+j]:
        if j >= 3:
            palindromes_odd.append(s[i-j:i+j+1])
        j += 1

#Even palindromes
for i in range(len(s)):
    j = 0
    while i - j >= 0 and i + j + 1 < len(s) and s[i-j] == s[i+j+1]:
        if j >= 3:
            palindromes_even.append(s[i-j:i+j+2])
        j += 1


print(len(palindromes_even))
print(len(palindromes_odd))    

print(palindromes_even)



