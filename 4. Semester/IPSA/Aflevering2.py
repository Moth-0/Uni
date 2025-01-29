"""
HANDIN 2 (palindrome)

This handin is done by: 
    202307989 Mikkel Moth Billing 

Reflection upon solution: 
    I used the method for the saxo file from the example, but had to add my path from the directory. 
    Then i start at finding strings with lenght 7, and then going up til lenght 10.
    To find palindromes, i use a for loop to check every letter and then n letters ahead. when i get to the end i go up 1 in string size.
    On line 24 i use 'range len(s) - n + 1', because i got a palindrome that was just s without, mabye because it goes out of bounds. 
"""
# From excerise description
from string import ascii_letters, digits
s = open('4. Semester\\IPSA\\saxo.txt', encoding='utf8').read()
s = s.lower()
s = ''.join([c for c in s if c in ascii_letters or c in digits])

# My Code
n = 7
while n < 11: 
    tal = 0
    for i in range(len(s) - n + 1):
        if s[i:i+n] == s[i:i+n][::-1]:
            tal += 1
            print(s[i:i+n])
    print("Number of pailindromes with lenght", n, ":", tal)
    n += 1
