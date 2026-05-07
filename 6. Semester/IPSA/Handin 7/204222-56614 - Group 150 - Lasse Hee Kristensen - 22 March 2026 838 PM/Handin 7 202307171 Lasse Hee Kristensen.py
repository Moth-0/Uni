#%%

'''
Jeg stater med at definere en funktion, der generer n tilfældige punkter i xy-planen. 
Funktionen tager et heltal n som input, og returnerer en liste af n tuples,
hvor hver tuple repræsenterer koordinaterne (x, y) for et punkt. 
Jeg bruger random() fra random til at generere koordinater mellem 0 og 1.

Så definerer jeg plot_hull funktionen, der skal tage en liste af punkter, og plotte dem,
men også tage et polygon og plotte det som en rød linje, der svarer til convex hull.
Med zip() pakkes x og y koordinaterne ud i to lister, så punkterne kan plottes.

Til sidst bruger vi left_turn funktionen til at bygge lower og upper hull.
Vi løber mod uret rundt om punkterne, og tjekker om 3 punkter laver danner
et vesntresving. Hvis de gøre, fjernes midterste punkt, da det så skal
ligge indeni convex hull. Punkterne combineres til at få hele convex hull.
Jeg tester et par cases med en docstring og bruger doctest
til at sørge for funktionen giver, hvad den skal. Assert sørger for 
at input er den rigtige datatype, punkterne har to koordinater i tuples,
og inden for det rigtige interval osv.
'''
from random import random

#a)
def random_points(n):

    assert 1<=n<=100 and isinstance(n, int), "n skal være heltal mellem 1 og 100"
    points = [(random(), random()) for _ in range(n)]
    return points

points = random_points(100)

#%%
#b)
import matplotlib.pyplot as plt

def plot_hull(points, polygon):

    xs, ys = zip(*points)
    xs_poly, ys_poly = zip(*polygon)

    #plot alle punkter
    plt.plot(xs, ys, 'go')

    #plot convex hull
    plt.plot(xs_poly, ys_poly , 'r-')
    plt.plot([xs_poly[-1], xs_poly[0]], #forbind første og sidste punkt
             [ys_poly[-1], ys_poly[0]], 'r-')
    return

#%% #c)

def left_turn(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1])    >= 0

def convex_hull(points):
    '''
    Beregner convex hull af en mængde punkter i xy-planen.

    >>> set(convex_hull([(0,0), (1,0), (0,1)])) == {(0,0),(1,0),(0,1)}

    >>> set(convex_hull([(0,0), (1,0), (1,1), (0,1), (0.5,0.5)])) == {(0,0),(1,0),(1,1),(0,1)}
    '''
    assert isinstance(points, list) and all(isinstance(p, tuple) and len(p) == 2 for p in points)

    points = sorted(set(points))

    if len(points)<=3: return points #trekant og mindre har kun én løsning

    lower_hull = []

    for p in points:
        lower_hull.append(p)
        while len(lower_hull) > 2 and left_turn(lower_hull[-3], lower_hull[-2], p):
            del lower_hull[-2]

    upper_hull = []

    for p in points[::-1]:
        upper_hull.append(p)
        while len(upper_hull) > 2 and left_turn(upper_hull[-3], upper_hull[-2], p):
            del upper_hull[-2]

    polygon = lower_hull[:-1] + upper_hull[:-1]
    return polygon

plot_hull(points, convex_hull(points))

#test trekant og internt punkt i kvadrat:
import doctest
doctest.testmod()
