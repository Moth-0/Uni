import numpy as np
import matplotlib.pyplot as plt
 
plt.rc("axes", labelsize=18, titlesize=22)   # skriftstørrelse af `xlabel`, `ylabel` og `title`
plt.rc("xtick", labelsize=16, top=True, direction="in")  # skriftstørrelse af ticks, vis også ticks øverst og vend ticks indad
plt.rc("ytick", labelsize=16, right=True, direction="in") # samme som ovenstående
plt.rc("legend", fontsize=16) # skriftstørrelse af figurers legends
 
#xlist = np.linspace(0, 50, num = 6)
xlist = np.array([0.0, 0.10, 0.20, 0.30, 0.40, 0.50])
ylist = np.array([1.685, 1.429, 1.165, 0.907, 0.648, 0.386])
 
a, b = np.polyfit(ylist, xlist, 1)
 
# Udskriver koefficienterne
print("a =", a)
print("b =", b)
 
plt.figure(num = 0, dpi =120)
plt.plot(ylist, a*ylist + b, label="Fit")
plt.plot(ylist, xlist, "o", label ="Data")
plt.title("Kalibrering")
plt.ylabel("Længde (m)")
plt.xlabel("Spænding (V)")
plt.legend()