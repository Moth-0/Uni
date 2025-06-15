'''
    POINTS

    Given a list with n points in the plane, compute for each pair of
    points if the Euclidean distance between the two points is <= distance.

    Input:  First line contains an integer distance >= 0.
            Second line contains a Python list of points, where each point
            is a tuple (x, y) of two integers. 2 <= len(points) <= 25

    Output: Print len(points) lines, each line containing len(points)
            characters, each either '*' or '.'. Character j in line i
            is '*' if the Euclidean distance between points[i] and
            points[j] is <= distance, otherwise '.'

    Example:

      Input:  2
              [(5, 5), (2, 2), (3, 3), (4, 4), (1, 1), (6, 6)]

      Output: *..*.*
              .**.*.
              .***..
              *.**..
              .*..*.
              *....*

              The first row corresponds to points[0] == (5, 5), and the three
              positions '*' correspond to points[0], points[3] and points[5],
              with distance 0, sqrt(2) and sqrt(2)=1.4142... to points[0]. 

    Note: The below code already reads distance and points from input.
'''


distance = int(input())
points = eval(input())

# insert code

pass

