#%%
'''
I a gemmer vi x, y som origo og vælger en tilfældig retning.
Alt efter retningen tillægges x eller y 1 eller -1 og den nuværende position
opdateres og yieldes, så next() af generatoren kan kaldes.
Generatoren kan bruges for så mange skridt, som man har lyst til.

i b) bruges islice til at stoppe generatoren efter 1000 skridt og gemme dem i 
en liste med det samme.

så oprettes et grid af nuller, hvor vi ved koordinaterne kan være i og bruger 
Counter til at tælle hvor mange gange hvert punkt optræder i path.
Hver frekvens for (x, y) indsættes i punktet grid[y, x] og imshow kaldes med grænserne
bestemt af min og max for x og y.
'''
#a)
import numpy as np

def random_walk():

    x, y = 0, 0

    while True:
        random_direction = np.random.choice(["up", "down", "left", "right"])
        if random_direction == "up":
            y += 1
        elif random_direction == "down":
            y += -1
        elif random_direction == "left":
            x -= 1
        elif random_direction == "right":
            x += 1
        yield (x, y)
            
gen = random_walk()

#%%
#b)

from itertools import islice 
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

#skærer generatoren af ved 1000 og gemmer det i en liste
path = list(islice(random_walk(), 1000))

xs, ys = zip(*path)
width = max(xs) - min(xs) + 1
height = max(ys) - min(ys) + 1

grid = np.zeros((height, width))
frequencies = Counter(path)

#udfyld grid med frekvensen af hvert punkt i path
for (x, y), freq in frequencies.items():
    grid[y - min(ys), x - min(xs)] = freq

plt.imshow(grid, extent=(min(xs), max(xs), min(ys), max(ys)))
plt.colorbar()
plt.show()
# %%

