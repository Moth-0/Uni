'''
HANDIN 2 (palindrome)

This handin is done by:

    202106248 Matilde E. Hansen
    202105331 Elias R. Skjoldborg

    Methood explained for even palindromes:
    We look for palindromes by running through the entire list one element at the time.
    For every element, we compare it and the previous 3 elements. This string of length 4 is then flipped and compared to the string made by 
    the following 4 elements (with no overlap). If the two strings are equal, we have found a palindromes of length 8.
    We then go into a recursive loop, where we run the same test, but where the strings are expanded by one element to the left and right
    respectivly. Every time this test succeds, we have found another palindromes that is longer by 2 elements. 
    The same procedure is used for the odd numbered palindromes, but where the first four elements are compared to the next four elements plus one.

    Note: The string "abcdeedcba" nets us two palindromes: "bcdeedcb" and "abcdeedcba"
'''
from string import ascii_letters, digits
s = open('saxo.txt', encoding='utf8').read()
s = s.lower()
s = ''.join([c for c in s if c in ascii_letters or c in digits])

summary = []
def sumsummer(string):      #Help function, so we can see how many palindromes we find of a given length
    L = len(string)
    print(string)
    for pair in summary:
        if pair[0] == L:
            pair[1] += 1
            break
    else:
        summary.append([L, 1])

counter = 0 # Total number of palindromes
# s = 'qwertyu_affabcdeOedcbaffa_wertyuio'      #Test string

def Block(left, right):               #Function that adds characters to a palidrome string to check if the paliendrome is part of a larger palindrome
        global counter
        counter += 1
        sumsummer(s[left+1:right])    #we add the palindrome to our summary

        done = False
        while done == False:
            if s[i:left-1:-1] == s[i+1:right+1]:       #Expand window we check in by one, 
                left -= 1
                right += 1

                counter += 1
                sumsummer(s[left+1:right])
            else:
                done = True


for i in range(0,len(s)):           #Here we search for the palindromes
    if len(s[i-4:i+5])>6 and s[i:i-4:-1] == s[i+1:i+5]:      #Looking for potential even palindromes of length 8 or greater
        left_edge = i-4
        right_edge = i+5
        Block(left_edge,right_edge)


    elif len(s[i-4:i+5])>6 and s[i-1:i-4:-1] == s[i+1:i+4]:      #Looking for potential odd palindromes of length 7 or greater
        left_edge = i-4
        right_edge = i+4

        Block(left_edge,right_edge)


print(counter)
print(summary)