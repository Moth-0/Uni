'''
HANDIN 2 (Palindrome)

This handin is done by Mathias Lystlund, id: 202408483:


Reflection upon solution:

    Checking for palindromes of a specific length was not that hard, because i could just
    turn it around with [::-1] and see if its a match. The hard part was checking for all palindromes
    with seven or more characters without being too slow. Then i heard about center expansion, which 
    greatly reduced the time. the principle is that a palindrome has a center, either an odd or an even one
    that we can expand from and then checking this sequence to see if its still a palindrome, this works
    really well.

'''
from string import ascii_letters, digits
s = open('saxo.txt', encoding='utf8').read()
s = s.lower()
s = ''.join([c for c in s if c in ascii_letters or c in digits])


pal = []          
N = len(s)

for center in range(N):
    L = center
    R = center
    while L >= 0 and R < N and s[L] == s[R]:
        if (R - L + 1) >= 7:
            pal.append((L, R, s[L:R+1]))
        L -= 1
        R += 1

    L = center
    R = center + 1
    while L >= 0 and R < N and s[L] == s[R]:
        if (R - L + 1) >= 7:
            pal.append((L, R, s[L:R+1]))
        L -= 1
        R += 1

print(len(pal))
