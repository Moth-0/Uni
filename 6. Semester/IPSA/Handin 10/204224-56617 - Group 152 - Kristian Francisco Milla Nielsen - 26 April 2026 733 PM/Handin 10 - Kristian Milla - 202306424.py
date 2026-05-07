'''''
This is done by :
748507 Kristian Milla

Reflection upon solution:
Den sværeste del var at transformere de rå koordinater (som kan være negative) 
til matrix-indekser, der starter ved 0. Og AI blev brugt til at hjælpe mig.
Til at håndtere den uendelige iterator, var itertools.islice nyttig til at 
udtrække 1000 datapunkter på en elegant måde.
'''

import random
import itertools
import collections
import matplotlib.pyplot as plt

def random_walk():
    x,y = 0,0 #startpunkt
    yield (x,y) 
    directions = [(1,0), (-1,0), (0,1), (0,-1)] #fire mulige skridt

    while True:
        dx,dy = random.choice(directions)
        x += dx
        y += dy
        yield (x,y)

walk = list(itertools.islice(random_walk(), 1000)) #Hent 1000 skridt ved hjælp af islice

counts = collections.Counter(walk) #Tæl hvor mange gange hver celle er besøgt

#Finder yderpunkterne for definere plot område
min_x = min(p[0] for p in walk)
max_x = max(p[0] for p in walk)
min_y = min(p[1] for p in walk)
max_y = max(p[1] for p in walk)

#Opretter en matrix fyldt med nuller. lægger 1 til størrelsen for at inkludere slutpunkterne
width = max_x - min_x + 1
height = max_y - min_y + 1
matrix = [[0] * width for _ in range(height)]

#Udfylder matrixen. bruger (x - min_x) som indeks for at undgå negative tal
for (x, y), freq in counts.items():
    matrix[y - min_y][x - min_x] = freq

plt.imshow(matrix, extent=[min_x, max_x, min_y, max_y], origin='lower') #'extent' sørger for at akserne viser de rigtige koordinater (f.eks. -10 til 15)
plt.colorbar(label='Antal besøg')
plt.title('Frekvens af besøg i Random Walk (1000 skridt)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()