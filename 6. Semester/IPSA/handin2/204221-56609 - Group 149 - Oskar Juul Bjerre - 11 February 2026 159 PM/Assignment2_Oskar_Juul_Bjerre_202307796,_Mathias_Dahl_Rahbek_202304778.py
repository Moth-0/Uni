'''
HANDIN 2 (palindrome)

202307796 Oskar Juul Bjerre
202304778 Mathias Dahl Rahbek 

Reflection upon solution: 

The idea for this solution was to treat every letter as the center of the text.
We look for a letter and expand outwards as long as the left and right letter
matched. This means we are skipping millions of non-palindrome matches, since
as soon as the left and right letter no longer matches, we stop searching.
We needed to create two distinct ways for the code to search for these
palindromes. Ones with an odd number of letters and one with an even number.
This is beacause, the starting point of each of these types of palindrome is 
different. One has to choose a "center point" containing a single letter, 
while the other had to choose a "center point" containg two letters. This 
caused us a bit of trouble in the beginning. 

'''

# Load in text file.
from string import ascii_letters, digits
s = open('saxo.txt', encoding='utf8').read()
s = s.lower()
s = ''.join([c for c in s if c in ascii_letters or c in digits])


substring_odd=[]
substring_even=[]
for i in range(len(s)): 
    t = s[i] # Look for palindromes of odd length
    u = s[i-1:i+1] # Look for palindromes of even length
    j = 0 
    k = 0 
    while t == t[::-1]: # Search for palindrome (odd)
        j+=1 # Increase index to look at next letter
        if len(t) >= 7: # Save palindromes of length >= 7
            substring_odd.append(t) 
        t=s[i-j:i+j+1] # Condition for next letter
    while u==u[::-1]: # Search for palindrome (even)
        if len(u) >=7:# Save palindromes of length >= 7
            substring_even.append(u)
        k+=1 # Increase index to look at next letter
    
        u=s[i-k-1:i+k+1] # Condition for next letter 

# Printing number of appearences 
print(f'There are {len(substring_odd)} of odd length')
unique_strings=[]
for t in substring_odd:
    ocurrences = substring_odd.count(t)
    if t not in unique_strings:
        unique_strings.append(t)
        print(f'{t} appears {ocurrences} time(s)')

print()
print(f'There are {len(substring_even)} of even length')
unique_strings=[]
for t in substring_even:
    ocurrences = substring_even.count(t)
    if t not in unique_strings:
        unique_strings.append(t)
        print(f'{t} appears {ocurrences} time(s)')






