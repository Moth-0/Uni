'''
    CAPITAL

    Write a function capital(text, words), that takes a string text and a list
    of strings words, and returns the same text, but with all words contained in
    words (when ignoring case) capitalized as stated in words.

    Input:  First line contains a text of at most 80 characters, with words
            separated by spaces (the text does not contain any punctuation marks).
            Second line contains at most 100 words separated by spaces.

    Output: A single line containing the same text as the first input line
            except for the capitalization stated by the second input line.

    Example:

      Input:  Iphone Samsung Oneplus and Lg produce mobile phones
              iPhone OnePlus Samsung LG

      Output: iPhone Samsung OnePlus and LG produce mobile phones

    Note: The below code already handles reading the input.
'''


def capital(text, words):
    # insert code
    D = {word.lower(): word for word in words}
    return ' '.join(D.get(word.lower(), word) for word in text.split())
             
            


text = input()
words = input().split()
print(capital(text, words))
