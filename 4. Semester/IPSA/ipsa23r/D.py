'''
    SWAPPING

    Your task is to write a function swapping(text) that takes a string text 
    and returns a string where every two consecutive characters are swapped,
    i.e., the first and second character are swapped, the third and fourth 
    character are swapped, etc. If the length of text is odd, the last
    character should be left unchanged.

    Input:  A single line with a non-empty text of length at most 50.

    Output: The same text with every two consecutive characters swapped.

    Example:

      Input:  ABCDEFGHIJK

      Output: BADCFEHGJIK

    Note: The below code already reads the input string and prints the result
          of calling the function swapping.
'''

def swapping(text):
    # insert code
    return ''.join(text[i:i+2][::-1] for i in range(0, len(text), 2)) 

print(swapping(input()))
