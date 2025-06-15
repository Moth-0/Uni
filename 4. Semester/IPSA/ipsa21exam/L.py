'''
    SAFE DISTANCE

    Your task is to write a function safe_distance(target, vectors), where
    target is a point/tuple (x, y) and vectors is a list of distinct vectors,
    each a tuple (x, y).  The function should return the smallest Euclidean
    distance from target to a point in the plane that is a sum of a subset
    of the vectors. 

    For target = (9, 10) and vectors = [(2, -5), (3, 4), (7, 3)],
    the point closest to target is (10, 7) = (3, 4) + (7, 3) with
    distance sqrt((9 - 10) ** 2 + (10 - 7) ** 2) = sqrt(10) = 3.162.

    Input:  A single line with a Python tuple (target, vectors).
            target is an integer tuple (x, y), with -100 <= x <= 100
            and -100 <= y <= 100, and vectors is a list of distinct
            integer tuples (x, y), with len(vectors) <= 50 and 
            -10 <= x <= 10 and -10 <= y <= 10.

    Ouput:  Distance from target to a closest point in the plane that
            is the sum of a subset of vectors.  The distance should be
            printed with 3 decimals.

    Example:

       Input:  ((9, 10), [(2, -5), (3, 4), (7, 3)])
 
       Output: 3.162

    Note: The below code already handles the input and output.
'''


def safe_distance(target, vectors):
    points = {(0, 0)}
    for x, y in vectors:
        points |= {(px + x, py + y) for px, py in points}
    x, y = target
    return (min((x - px) ** 2 + (y - py) ** 2 for px, py in points))**(1/2)

target, vectors = eval(input())
distance = safe_distance(target, vectors)
print('%.3f' % distance)
