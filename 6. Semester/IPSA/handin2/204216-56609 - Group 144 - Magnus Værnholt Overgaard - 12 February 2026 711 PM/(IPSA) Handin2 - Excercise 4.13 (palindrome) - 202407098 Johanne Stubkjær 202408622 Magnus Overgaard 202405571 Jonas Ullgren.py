# Gerth's code (loads the txt-file, makes all letters lower case, compiles all the letters to 1 string)
from string import ascii_letters, digits

s = open('saxo.txt', encoding='utf8').read()
s = s.lower()
s = ''.join([c for c in s if c in ascii_letters or c in digits])


# Our code to solve the problem....

from collections import Counter

def count_palindromes(data, min_pal_len, max_pal_len, print_sorted_palindromes=False):
    palindromes = []
    max_odd_radius  = (max_pal_len - 1) // 2
    max_even_radius = max_pal_len // 2 - 1
    n = len(data)
    
    for c in range(n):
        # Check for odd palindromes ("abcba"):
        for j in range(max_odd_radius+1):
            scan_L, scan_R = c-j, c+j
            
            if scan_L<0 or scan_R>=n: 
                break  # Avoids "index out of range" error that arise if expanding goes outside string
            
            if data[scan_L] != data[scan_R]:
                break  # If the characters don't match it is not a palindrome, so break

            length_odd = 2*j+1
            if length_odd >= min_pal_len:
                palindromes.append(data[scan_L:scan_R+1]) # scan_R+1 because this indexing excludes the end value
    
        # Check for even palindromes ("abccba"):
        for k in range (max_even_radius+1): # New loop to avoid them "breaking" each other
            scan_L, scan_R = c-k, c+k+1
            
            if scan_L<0 or scan_R>=n: 
                break

            if data[scan_L] != data[scan_R]:
                break

            length_even = 2*k+2
            if length_even >= min_pal_len:
                palindromes.append(data[scan_L:scan_R+1])

    length_counts = Counter(len(p) for p in palindromes) # Counts up the amount of palindromes of each length
    for i in range(min_pal_len, max_pal_len+1): 
        print(f"Palindromes of length {i}:   {length_counts[i]}")
    
    print(f"Palindromes in total:      {len(palindromes)}")

    if print_sorted_palindromes == True:  # If this is set to true in the function, print the list sorted by length
        print()
        print(sorted(palindromes, key=len))


"""
The excercise tells us to look for palindromes of length >= 7, but we also know there aren't any larger than 10 (of which there is 1 of). In the function it does not matter if we put 10 or 1000 as the largest palindrome length. This is because the function terminates whenever it "sees" that the one it is checking is not a palindrome. Another excercise could ask us to look for palindromes of length in a certain interval [a,b], so therefor we implemented this as an option. Both are shown below.
"""

# Example of finding palindromes in a certain interval
#count_palindromes(s, 4, 6)

# What the handin asks us to find (printed and ordered by length):
count_palindromes(s, 7, 10, True)