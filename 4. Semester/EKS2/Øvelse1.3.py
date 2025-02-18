# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Plot settings
plt.rc("axes", labelsize=18, titlesize=22)   # skriftstørrelse af `xlabel`, `ylabel` og `title`
plt.rc("xtick", labelsize=16, top=True, direction="in")  # skriftstørrelse af ticks, vis også ticks øverst og vend ticks indad
plt.rc("ytick", labelsize=16, right=True, direction="in") # samme som ovenstående
plt.rc("legend", fontsize=16) # skriftstørrelse af figurers legends

#Functioner 
def find_θ2(θ1):
    return np.arcsin(n_glas/n_luft * np.sin(θ1))

def Rs_func(θ1): 
    return np.sin(θ1 - find_θ2(θ1))**2 / np.sin(θ1 + find_θ2(θ1))**2

def Rp_func(θ1):
    return np.tan(θ1 - find_θ2(θ1))**2 / np.tan(θ1 + find_θ2(θ1))**2

def Ts_func(θ1):
    return np.sin(2*θ1)*np.sin(2*find_θ2(θ1))/np.sin(θ1+find_θ2(θ1))**2

def Tp_func(θ1):
    return np.sin(2*θ1)*np.sin(2*find_θ2(θ1))/np.sin(θ1+find_θ2(θ1))**2/np.cos(θ1-find_θ2(θ1))**2

# Brydningsindex
# n_{glas} = n_{luft} * sin(θ_1) / sin(θ_2)

baggrund = 0.0366
n_glas = 1.5
n_luft = 1.0

θ1_list = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 42, 43, 44, 45,50,55,60])
print(θ1_list[3:-3])

φ2_list = np.array([172, 169.5, 166, 162.2, 158, 151, 146, 142.2, 135.2])
φ2_list = 180 - φ2_list

θ2_list = θ1_list[3:-4] + φ2_list

φ1_list = np.array([26.5, 36.5, 47, 58, 66.5, 76.2, 80.9, 82.9, 84.2, 86.7, 97, 107, 112])

θ1_lin = np.linspace(0, 90, 1000)

n_g_list = np.sin(np.deg2rad(θ2_list)) / np.sin(np.deg2rad(θ1_list[3:-4]))
n_g_teori = np.average(n_g_list)

print(f'n_glas_teori = {n_g_teori}')


# Transmittet
T_s = np.array([2.464, 2.114, 2.008, 1.785, 2.332, 1.429, 2.262, 1.988, 2.383, 1.992, 1.722, 0.632]) - baggrund
T_p = np.array([2.297, 2.692, 1.944, 1.848, 2.181, 1.329, 1.973, 1.682, 1.862, 1.397, 1.108, 0.333]) - baggrund

# Reflekteret
R_s = np.array([0.085, 0.073, 0.054, 0.047, 0.030, 0.055, 0.177, 0.370, 1.109, 1.757, 1.747, 2.198, 1.841]) - baggrund
R_p = np.array([0.114, 0.117, 0.127, 0.233, 0.239, 0.450, 0.623, 0.912, 1.530, 2.088, 2.011, 1.972, 2.252]) - baggrund

R_s = R_s/T_s[0]
R_p = R_p/T_p[0]

T_s = T_s/T_s[0]
T_p = T_p/T_p[0]

# Plot reflekteret som funktion af indfaldsvinkel
plt.plot(θ1_list[3:-3], R_s[:-3], "o", label=r'$R_s$')
plt.plot(θ1_list[3:-3], R_p[:-3], "o",  label=r'$R_p$')

# Plot teori
plt.plot(θ1_lin, Rs_func(np.deg2rad(θ1_lin)), label=r'$R_s$ teori')
plt.plot(θ1_lin, Rp_func(np.deg2rad(θ1_lin)), label=r'$R_p$ teori')

# Udregn Brewsters vinkel og plot
θ_B = np.arctan(n_luft/n_g_teori)
print(f"Brewster angle = {θ_B}")
plt.plot([np.rad2deg(θ_B), np.rad2deg(θ_B)], [0.0, 0.05], color='r', linestyle='--', label='Brewster Angle')

# Critical angle (kun for n1 > n2, så glas -> luft)
θ_C = np.arcsin(n_luft/n_g_teori)
print(f"Critical angle = {θ_C}")
plt.plot([np.rad2deg(θ_C), np.rad2deg(θ_C)], [0.0, 0.05], color='b', linestyle='--', label='Critical Angle')


# Plot settings
plt.xlim(10, 60)
plt.ylim(0, 1.3)
plt.xlabel(r'Incident Angle $(θ_1)$')
plt.ylabel('Reflectance')
plt.title('Reflectance vs Incident Angle')
plt.legend(fontsize=12)
plt.show()

# Plot transmiterede som funktion af indfaldsvinkel
plt.plot(θ1_list[:-4], T_s, "o", label=r'$T_s$')
plt.plot(θ1_list[:-4], T_p, "o",  label=r'$T_p$')

# Plot teori
plt.plot(θ1_lin, Ts_func(np.deg2rad(θ1_lin)), label=r'$T_s$ teori')
plt.plot(θ1_lin, Tp_func(np.deg2rad(θ1_lin)), label=r'$T_p$ teori')

# Plot settings
plt.xlim(10, 60)
plt.ylim(0, 1.3)
plt.xlabel(r'Incident Angle $(θ_1)$')
plt.ylabel('Reflectance')
plt.title('Reflectance vs Incident Angle')
plt.legend(fontsize=12)
plt.show()

print(T_s+R_s)
print(T_p+R_p)