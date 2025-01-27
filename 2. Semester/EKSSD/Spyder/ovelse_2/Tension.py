import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
 
plt.rc("axes", labelsize=18, titlesize=22)   # skriftstørrelse af `xlabel`, `ylabel` og `title`
plt.rc("xtick", labelsize=16, top=True, direction="in")  # skriftstørrelse af ticks, vis også ticks øverst og vend ticks indad
plt.rc("ytick", labelsize=16, right=True, direction="in") # samme som ovenstående
plt.rc("legend", fontsize=16) # skriftstørrelse af figurers legends
 
#xlist = np.linspace(0, 50, num = 6)
dl_l = np.array([0.0, 0.02, 0.04, 0.06, 0.08])
kraft_l = np.array([3.25, 2.93, 2.88, 2.48, 2.20])
L_l = 0.3+dl_l

def T1(L, Lp, Mp): 
    return Lp*Mp*9.82/L
def T2(dL, L, Lp, Mp):
    return Lp*Mp*9.82/(L+dL)

gæt = [0.2 , 0.2, 0.6]

popt, pcov = curve_fit(T2, dl_l, kraft_l, p0=gæt)

# Udskriver koefficienterne
print(f"L = {popt[0]:.3f} m, Lp = {popt[1]:.3f} m, Mp = {popt[2]:.3f} kg")
 
plt.plot(dl_l, T2(dl_l, *popt), label="Fit")
plt.plot(dl_l, T2(dl_l, *gæt), label ="Gæt")
plt.plot(dl_l, kraft_l, "o", label="Data")
plt.title("Tension")
plt.xlabel("Længde (m)")
plt.ylabel("Kraft (N)")
plt.legend()
