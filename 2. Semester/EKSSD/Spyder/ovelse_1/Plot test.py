# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import IPython

def f(x, A, B, C):
        return A*x**2+B*x+C
    
xlist = np.linspace(0, 10, num = 100)

ylist = f(xlist, 2,3,4)

plt.figure(num = 0, dpi =120)
plt.plot(xlist, ylist, label ="Indsæt datanavn for graf 1 her")
plt.plot(xlist, ylist**1.1, label ="Indsæt datanavn for graf 2 her")
plt.title("Titel")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.legend()
