from random import randint
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from itertools import islice

'''
HANDIN 10 (Random Walk)

This handin is done by (study ids and names of up to three students):

    202407458 Kenny Nguyen
    202408911 Safiya Chebil 
    202406237 Marie Schnoor - Madsen 

    
Reflection upon solution:
Det svære har været at sikre at man kun må rykke sig i et punkt enten x eller y retningen. 
Vi havde problemer med imshow så brugte hist2d istedet. 

'''

def random_walk (point=(0,0)):
    
    while True:
        x, y = point
        
        x_or_y = random.choice(point)
        
        val = random.choice((x_or_y-1,x_or_y+1))
        
        if x_or_y == x:
            point = (val,y)
        else:
            point = (x,val)
            
        yield(point)  


walk = random_walk()

listrx = list(islice(walk, 0, 10))
print(listrx)

#extracting allthe points
listy =[(0,0)]
i=0
while i<=1000:
    point = next(iter(walk))
    listy.append(point)
    i+=1

#extracting the x and y koordiantes seperately to use in hist2d
listy = np.array(listy)
x = listy[:, 0]
y = listy[:, 1]
x,y

fig, ax = plt.subplots()
val = 100
h = ax.hist2d(x, y, bins=20, cmap='RdPu')#, range = [[-val, val], [-val, val]])
fig.colorbar(h[3], ax=ax)
plt.show()