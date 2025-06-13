'''
    CAPITALS

    Remove all lower case letters from a string.

    Input:  A single line with a string containtin lower and capital letters,
            and length between 1 and 100.

    Output: The input string with all lower case letters removed.

    Example:

      Input:  ComeLateAndStartSleeping

      Output: CLASS
'''


# insert code
string = input()
out = ""

for l in string: 
    if l.isupper(): 
        out += l

print(out)