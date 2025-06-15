'''
    STARS

    Your task is to create a function 'print_stars', that given a list
    of (name, score) prints each name followed by score copies of '*'. 
    All names should be appended by underscores '_', so that all names
    become equal length. A single additional '_' should be printed 
    between names and stars.

    Example:
    
        stars = [('JOHN', 2), ('JOE', 3), ('ALEXANDER', 2), ('VICTOR', 0), ('ALBERT', 5)]
        print_stars(stars)

    example output:

        JOHN______**
        JOE_______***
        ALEXANDER_**
        VICTOR____
        ALBERT____*****

    The function print_stars should take two optional keyword arguments
    'alphabetically' and 'highscore', such that

        print_stars(stars, alphabetically=True)

    prints the names in alphabetically order, whereas 

        print_stars(stars, highscore=True)

    prints the names sorted in decreasing score order, where names with
    equal score should be printed alphabetically (see test files for
    examples). If neither alphabetically or highscore are True, names
    should be printed in the order given in the input.

    Finally, print_stars should accept an optional argument 'vertical',
    that prints the scores vertically (and can be combined with arguments
    highscore and alphabetically). See example below. Each name is printed
    top-down with stars above, and underscores below and above to make
    all columns have equal length and names starting in same row.
    All rows should have equal length, and score columns separated by
    underscores.

    Example:

        print_stars(start, vertical=True, highscore=True)

    example output:
    
        *________
        *________
        *_*______
        *_*_*_*__
        *_*_*_*__
        A_J_A_J_V
        L_O_L_O_I
        B_E_E_H_C
        E___X_N_T
        R___A___O
        T___N___R
        ____D____
        ____E____
        ____R____

    Input:  A single Python expression calling print_stars.
            At most one of the keyword arguments alphabetically
            and highscore will be True.
            There are 1..20 distinct names.
            Each name as length 1-20 and contains only characters A-Z.
            Scores are integers 0..5.

    Output: The result of calling print_stars.

    Note: The below code already reads the input and calls print_stars.
'''


def print_stars(stars):
    # insert code

    pass  


eval(input())
