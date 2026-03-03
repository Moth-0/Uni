"""
HANDIN 2 (palindrome)

This handin is done by: 
    202307989 Mikkel Moth Billing 

Reflection upon solution: 
    I used the method for the saxo file from the example, but had to add my path from the directory. 
    Then i start by finding strings with lenght 7, and then going up til lenght 10.
    To find palindromes, i use a for loop to check every letter and then n letters ahead. when i get to the end i go up 1 in string size.
    On line 24 i use 'range len(s) - n + 1', because i got a palindrome that was just s, mabye because it goes out of bounds. 
"""
# From excerise description
from string import ascii_letters, digits
s = open(r'saxo.txt', encoding='utf8').read()
s = s.lower()
s = ''.join([c for c in s if c in ascii_letters or c in digits])*10

import time

def time_it(f):
    def wrapper(*args, **kwargs):
        t_start = time.time()
        result = f(*args, **kwargs)
        t_end = time.time()
        t = t_end - t_start
        print(f'{f.__name__} took {t:.2f} seconds')
        return result
    return wrapper

# My Code
@time_it
def mine(s=s, n=7, e=11):
    a = 0
    while n < e+1:                           # Go up til 10 letters
        tal = 0
        for i in range(len(s) - n + 1):     # Go throught the index of the string
            if s[i:i+n] == s[i:i+n][::-1]:  # If the string of n letters is the same as
                tal += 1                    # the reverse, add a counter and print the string
                #print(s[i:i+n])
        print("Number of pailindromes with lenght", n, ":", tal)
        a += tal
        n += 1                              # Go up 1 in string size

    print(f'Sum = {a}')

@time_it
def gerth(s, n=7, e=11):
    count = 0
    for i in range(len(s)):
        for j in range(i + n, i + e):
            t = s[i:j]
            if t == t[::-1]:
                count += 1
    print(count)

@time_it
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

find_palindromes(s)