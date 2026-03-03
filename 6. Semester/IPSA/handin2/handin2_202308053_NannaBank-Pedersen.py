'''
HANDIN 2 (palindrome)

This handin is done by:
    202308053 Nanna Bank-Pedersen

Reflection upon solution:
The most challenging part of this exercise was understanding how to find
palindromes by looking around a middle position for both
odd and even lengths. Designing the dictionary manually
to count palindromes and store the distinct palindromes was also a bit tricky.
My code assumes the input is a single long string of letters and digits.
A limitation is that the code may be slow in the worst case for very
repetitive text, but it works well for normal input and was easy to understand.
'''
from string import ascii_letters, digits

s = open('handin2\saxo.txt', encoding='utf8').read()
s = s.lower()
s = ''.join(c for c in s if c in ascii_letters or c in digits)

n = len(s)
MIN_LEN = 7

total = {}
distinct = {}

# Odd
for middle in range(1, n - 1):
    k = 1
    while middle - k >= 0 and middle + k < n:
        if s[middle - k] != s[middle + k]:
            break

        length = 2 * k + 1
        if length >= MIN_LEN:
            if length not in total:
                total[length] = 0
                distinct[length] = set()

            p = s[middle - k : middle + k + 1]
            total[length] += 1
            distinct[length].add(p)

        k += 1

# Even
for left_middle in range(n - 1):
    if s[left_middle] != s[left_middle + 1]:
        continue

    k = 0
    while left_middle - k >= 0 and left_middle + 1 + k < n:
        if s[left_middle - k] != s[left_middle + 1 + k]:
            break

        length = 2 * (k + 1)
        if length >= MIN_LEN:
            if length not in total:
                total[length] = 0
                distinct[length] = set()

            p = s[left_middle - k : left_middle + 2 + k]
            total[length] += 1
            distinct[length].add(p)

        k += 1

for length in sorted(total):
    print(
        f"{total[length]} palindromes of length {length} "
        f"({len(distinct[length])} distinct)"
    )