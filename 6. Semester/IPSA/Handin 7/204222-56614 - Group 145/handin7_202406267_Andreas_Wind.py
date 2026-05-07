'''
HANDIN (convex hull)

This handin is done by (study ids and names of up to three students):

    202406267 Andreas Wind

Reflection upon solution:
    
    Det var virkelig svært at få kanten til at ramme de rigtige punkter,
    da man lige skulle forstå hvilken vej det skulle gå og også hvordan
    den der left-turn funktion fungerede.
    Derudover syntes jeg at det var ret svært at lave assert og doctest
    da det ikke er noget jeg har prøvet før. Derfor fik jeg hjælp af AI
    til det. Jeg føler at jeg forstår det nu, men har nok brug for lidt
    uddybning af nogle ting til TØ.
'''

from random import random
import matplotlib.pyplot as plt
import doctest

def left_turn(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]) >= 0

def convex_hull(points):
    """
    Regner convex hull
    
    >>> points = [(3,2), (1,1), (2,3), (2,2), (1.5, 2.25), (2.5, 2.25), (2, 1.25), (1, 1.5)]
    >>> convex_hull(points)
    [(1, 1), (1, 1.5), (2, 3), (3, 2), (2, 1.25)]
    """

    points = sorted(points)

    lower = []

    # går listen af points igennem og appender, men hvis lower er længere end 2
    # og hvis der er et left turn, så fjernes det element hvori der er left turn
    for p in points:
        while len(lower) >= 2 and left_turn(lower[-2], lower[-1], p):
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points): # går højre om i stedet for venstre om
        while len(upper) >= 2 and left_turn(upper[-2], upper[-1], p):
            upper.pop()
        upper.append(p) 


    return lower[:-1] + upper[:-1]


def random_points(n):
    output_points = []

    for i in range(n):
        output_points.append((random(), random()))
    
    return output_points

def plot_hull(points, polygon):
    x,y = zip(*points)
    plt.plot(x, y, 'go', label='Input points')

    #tilføjer det første punkt til sidst for at "lukke" figuren
    closed_polygon = polygon + [polygon[0]]
    px, py = zip(*closed_polygon)
    plt.plot(px, py, 'r-', label='Convex Hull')
    plt.plot(px, py, 'ro')

    plt.legend()
    plt.show()
    

    
# nu laver jeg doctest:


if __name__ == "__main__":
    doctest.testmod()

    # test-data fra opgaven
    points = [(3,2), (1,1), (2,3), (2,2), (1.5, 2.25), (2.5, 2.25), (2, 1.25), (1, 1.5)]
    CH = convex_hull(points)
    
    # tjekker om CH er et subset af points
    for p in CH:
        assert p in points, f"Punktet {p} er ikke i den oprindelige liste"

    # tjekker om CH[0] er det mindste punkt
    assert CH[0] == min(points), "Det første punkt er ikke det mindste"

    # tjekker at der er mindst 3 punkter i hull
    assert len(CH) >= 3, "Hull skal have mindst 3 punkter"

    print("Alle tests bestået")

    plot_hull(points, CH)