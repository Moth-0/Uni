import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
 
plt.rc("axes", labelsize=18, titlesize=22)   # skriftstørrelse af `xlabel`, `ylabel` og `title`
plt.rc("xtick", labelsize=16, top=True, direction="in")  # skriftstørrelse af ticks, vis også ticks øverst og vend ticks indad
plt.rc("ytick", labelsize=16, right=True, direction="in") # samme som ovenstående
plt.rc("legend", fontsize=16) # skriftstørrelse af figurers legends
 
#xlist = np.linspace(0, 50, num = 6)
t_list = np.array([89, 74, 60, 50, 41, 1, 344-360, 318-360, 300-360, 270-360])
v_list = np.array([2.604, 2.508, 2.185, 2.048, 1.725, 0.0014, -1.52, -3.675, -5.16, -6.76])

v_a = np.linspace(-7, 3, 1000)
t_a = np.linspace(-90,90, 1000)

def g(V, a,b,c,d): 
    return -1/c*np.log(1/b*(a/(V+d)-1))
    
def h(t, a,b,c,d):
    return a/(1+b*np.exp(-c*t))-d

popt, pcov = curve_fit(h, t_list, v_list, p0=np.array([1,1,1,1]))
a,b,c,d = popt
print(a,b,c,d)
 
# Udskriver koefficienterne
#print("a =", a)
#print("b =", b)

fig, [ax1, ax2] = plt.subplots(1,2, figsize=(8,4))

ax1.plot(t_list, v_list, label ="Data")
ax1.plot(t_a, h(t_a, a,b,c,d), label ="Fit")
ax1.plot(t_a, h(t_a, 1, 1, 1, 1), label="Gæt")
ax1.set_title("Kalibrering")
ax1.set_xlabel("Vinkel (grader)")
ax1.set_ylabel("Spænding (V)")
ax1.legend()


ax2.plot(v_list, t_list, label ="Data")
ax2.plot(v_a, g(v_a, a,b,c,d), label ="Fit")
ax2.set_title("Kalibrering")
ax2.set_ylabel("Vinkel (grader)")
ax2.set_xlabel("Spænding (V)")
ax2.legend()

plt.tight_layout()