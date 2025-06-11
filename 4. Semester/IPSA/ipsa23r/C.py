'''
    PYRAMID

    Your task is to read a line of text and print it as a pyramid, i.e., the 
    last output line is the input text, and each line above it is the line below
    it with the first and last character removed. Removed characters should 
    be printed as '.'. The first line contains either one or two input 
    characters, depending on if n is odd or even. 

    For the string ABCDEFGHIJKLMNOPQRSTUVWX of length 24 the output should be:

        ...........LM...........
        ..........KLMN..........
        .........JKLMNO.........
        ........IJKLMNOP........
        .......HIJKLMNOPQ.......
        ......GHIJKLMNOPQR......
        .....FGHIJKLMNOPQRS.....
        ....EFGHIJKLMNOPQRST....
        ...DEFGHIJKLMNOPQRSTU...
        ..CDEFGHIJKLMNOPQRSTUV..
        .BCDEFGHIJKLMNOPQRSTUVW.
        ABCDEFGHIJKLMNOPQRSTUVWX

    Input:  A string with n characters, where 1 <= n <= 25.

    Ouput: The pyramid of the input string, i.e., ceil(n / 2) lines, each 
           containing the n characters as described above.

    Examples:

      Input: 123456789
    
      Ouput: ....5....
             ...456...
             ..34567..
             .2345678.
             123456789
'''


# insert code
from math import ceil
string = input()
n = len(string)

for i in reversed(range(ceil(n / 2))):
    print('.'*i + string[i:n-i] + '.'*i)
