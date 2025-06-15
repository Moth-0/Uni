'''
    PROTECTED

    You are given a rectangular area with a length and width. You want to
    protect it by adding a protection zone around the area of a given width
    and print the total area required.
    
    In the below example the area has length 12, width 3, and the protection
    zone has width 2. The total area including the protection zone is 
    16 * 7 = 112.

        ZZZZZZZZZZZZZZZZ
        ZZZZZZZZZZZZZZZZ
        ZZ............ZZ
        ZZ............ZZ
        ZZ............ZZ
        ZZZZZZZZZZZZZZZZ
        ZZZZZZZZZZZZZZZZ

    Input:  Three integers, length, width, and zone, separated by space.
            The length and width are integers between 1 and 100, and the zone
            width is an integer between 0 and 100.

    Output: The total area including the protection zone.

    Example:

      Input:  12 3 2

      Output: 112 
'''


# insert code
l, w, p = map(int, input().split())

print((l+2*p)*(w+2*p))
