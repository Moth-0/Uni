'''
This is done by :
748507 Kristian Milla

Reflection upon solution:
Jeg kunne nok godt have lavet random_points forenklet med en list comprehension.
Implementeringen af det konvekse hylster (Convex Hull) var både udfordrende og spændende. 
Det var særligt lærerigt at forstå "elastik-konceptet" gennem Andrew’s Monotone Chain algoritme.
Sorteringen af punkterne var her en nøgleforudsætning. 
Den sværeste del var at sikre korrekt testning af koden; her var doctest og assert dog meget hjælpsomme 
til at verificere, at algoritmen håndterer både punkter i midten og punkter på rette linjer korrekt.
'''

import random

def random_points(n):
    points = []
    for _ in range(n):
        x = random.random()
        y = random.random()
        points.append((x, y))
    return points

import matplotlib.pyplot as plt

def plot_hull(points, polygon):
    x, y = zip(*points)
    px, py = zip(*polygon)
    px = list(px)
    py = list(py)
    px.append(px[0]) # Lukker polygonen ved at forbinde sidste punkt med første
    py.append(py[0])
    plt.plot(x, y, 'o')
    plt.plot(px, py, '-')
    plt.show()

def left_turn(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]) >= 0

def convex_hull(points):
    #Sorter punkterne leksikografisk (først på x, så på y)
    n = len(points)
    if n <= 2:
        return points
    sorted_points = sorted(points)

    #Beregn den øvre del (Upper Hull)
    upper = []
    for p in sorted_points:
        while len(upper) >= 2 and left_turn(upper[-2], upper[-1], p):
            upper.pop()
        upper.append(p)

    # Vi gør det samme, men går gennem punkterne i omvendt rækkefølge
    lower = []
    for p in reversed(sorted_points):
        while len(lower) >= 2 and left_turn(lower[-2], lower[-1], p):
            lower.pop()
        lower.append(p)

    return upper[:-1] + lower[:-1]

import doctest

def test_convex_hull():
    # Test 1: En simpel firkant
    input_points = [(0,0), (2,0), (2,2), (0,2), (1,1)]
    result = convex_hull(input_points)
    assert len(result) == 4, f"Forventede 4 punkter, fik {len(result)}"
    assert (1,1) not in result, "Punktet (1,1) burde være inde i hylsteret"
    
    # Test 2: Punkter på en ret linje (skal håndteres af left_turn >= 0)
    line_points = [(0,0), (1,0), (2,0), (1,1)]
    result_line = convex_hull(line_points)
    # Da left_turn bruger >= 0, vil punkter på linjen blive fjernet
    assert len(result_line) == 3 
    
    print("Alle assert-tests bestået!")

if __name__ == "__main__":
    # Hvis alt er OK, skriver den ingenting. Hvis der er fejl, får man besked.
    doctest.testmod(verbose=True)
    # Kør vores manuelle assert-tests
    test_convex_hull()

points = random_points(95)
hull = convex_hull(points)
plot_hull(points, hull)    