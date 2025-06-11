'''
    REPLACE

    Write a function replace(text, substitutes) that takes a string text 
    consisting of space separated words and a dictionary substitutes,
    that consists of key-value pairs where both the key and the value are
    single words, returns a new string where each word in the text, that is a 
    key in substitutes, is replaced by the associated word in the dictionary.
    
    E.g., if 
    
       text = 'COPENHAGEN IS GREAT' and 
       substitutes = {'COPENHAGEN': 'AARHUS', 'GREAT': 'FANTASTIC'}, 

    then the function replace should return 'AARHUS IS FANTASTIC'.

    Input:  Two lines. The first line contains a text consisting of space
            separated words. The second line contains a Python dictionary 
            substitutes containing the possible string replacements.
            All words in the text, and keys and values in the dictionary 
            are single words containing upper case letters only.

    Output: The result of calling replace(text, substitutes).

    Example:

      Input:  COPENHAGEN IS GREAT
              {'COPENHAGEN': 'AARHUS', 'GREAT': 'FANTASTIC'}

      Output: AARHUS IS FANTASTIC

    Note: The below code already reads the input and calls replace.
'''


def replace(text, substitutes):
    # insert code
    text_list = text.split(' ')
    for i in range(len(text_list)): 
        for key in substitutes: 
            if text_list[i] == key: 
                text_list[i] = substitutes[key]

    return " ".join(text_list)


text = input()
replacements = eval(input())
print(replace(text, replacements))
