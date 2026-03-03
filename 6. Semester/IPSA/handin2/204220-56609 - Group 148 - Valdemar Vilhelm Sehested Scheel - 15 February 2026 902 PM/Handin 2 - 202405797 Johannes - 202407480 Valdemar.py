'''
HANDIN 2 (Palindrome)

This handin is done by:

    202405797 Johannes Bøgh Fangel
    202407480 Valdemar V. S. Scheel


    For ease, the code was made to work with any type of string with removed formatting and no numbers. 
    This meant it could be tested on a self made string.
    It was also with this self-made string the palindrome checker was adjusted with. 
    It took a bit of time to figure out exactly how to invert the string without saving it as a variable each time.
    We made an empy list to add the palindromes to so we could just take the lenght of it to count the end result.
    We also made it variable at what lenght it should start checking and when it should start.
    There might be some limit problems when it is checking for the palindromes, 
    but thankfully there weren't any of the ones we needed to check at the end of the string. 
    I could adjust the limit for the while loop to fix it, but it seems unnecessary since it works. 
    It would just be adjusting using the lenght of the palindrome we're checking for.
    
'''

from string import ascii_letters, digits
s = open('saxo.txt', encoding='utf8').read()
s = s.lower()
s = ''.join([c for c in s if c in ascii_letters or c in digits])


string = s   # This is just a way of inserting an arbitrary string into the loop below. 
list_of_palindromes = []     # This is an array that keeps track of palindromes
stop_len_of_palindrome = 10  # Stop lenght of palindrom. We stop when it checks for palindromes of lenghts 10
len_of_palindrome_check = 7  # Start lenght it checks for

for i in range(len(string)):
    if len_of_palindrome_check > stop_len_of_palindrome:  #Just a loop stopper
        print(f"Amount of palindromes in the text: {len(list_of_palindromes)}")
        break
    j = 0 #Resets for very i
    while j<=len(string):
        if j+len_of_palindrome_check <= len(string)-1 and string[j:j+len_of_palindrome_check:1] == string[j+len_of_palindrome_check-1:j-1:-1]:
            #If our string part fulfills its lenght being inside the whole string and it being symmetric, it then gets appended into our list.
            list_of_palindromes.append(string[j:j+len_of_palindrome_check])
        j += 1 # Updates checking point
        
    len_of_palindrome_check += 1 #Increases the lenght of the palindromes it checks for


print(list_of_palindromes)     


# It can check for palindromes with lenght 2.