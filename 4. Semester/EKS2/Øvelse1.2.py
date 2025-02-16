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
    return np.arcsin(n_luft/n_glas * np.sin(θ1))

def Rs_func(θ1): 
    return np.sin(θ1 - find_θ2(θ1))**2 / np.sin(θ1 + find_θ2(θ1))**2

def Rp_func(θ1):
    return np.tan(θ1 - find_θ2(θ1))**2 / np.tan(θ1 + find_θ2(θ1))**2

# Brydningsindex
# n_{glas} = n_{luft} * sin(θ_1) / sin(θ_2)

baggrund = 0.0366
n_glas = 1.5
n_luft = 1.0

θ1_list = np.array([0, 15, 20, 25, 30,35,40,45,50,55,60,65,70,75,80,85,90])

φ2_list = np.array([180, 28, 174,172,171,172,174,176,178,161,164,167,151,155,141,145,178])
θ2_list = θ1_list - φ2_list

θ1_lin = np.linspace(0, 90, 1000)

n_g_teori = np.sin(np.average(np.deg2rad(θ1_list))) / np.sin(np.average(np.deg2rad(θ2_list)))

print(n_g_teori)


# Transmittet
T_s = np.array([4.98, 5.13, 5.18, 5.16, 5.17, 4.92, 5.11, 4.805, 4.437, 4.429, 4.541, 3.842, 3.400, 2.744, 1.599, 0.472, 5.148])
T_p = np.array([4.88, 4.37, 4.52, 4.48, 4.64, 4.07, 4.45, 4.411, 4.19, 4.15, 4.539, 4.059, 3.825, 3.303, 2.198, 0.715, 5.148])

# Reflekteret
R_s = np.array([0, 0.122,0.207, 0.232, 0.282, 0.285, 0.343, 0.48, 0.477, 0.604, 0.878, 1.136, 1.456, 2.268, 3.216, 4.638, 5.148])
R_p = np.array([0, 0.122, 0.159, 0.146, 0.122, 0.096, 0.09, 0.066, 0.017, 0.004, 0.005, 0.0064, 0.166, 0.444, 1.040, 2.339, 5.148])

R_s = R_s/R_s[-1]
R_p = R_p/R_p[-1]

# Plot reflekteret som funktion af indfaldsvinkel
plt.plot(θ1_list, R_s, "o", label=r'$R_s$')
plt.plot(θ1_list, R_p, "o",  label=r'$R_p$')

# Plot teori
plt.plot(θ1_lin, Rs_func(np.deg2rad(θ1_lin)), label=r'$R_s$ teori')
plt.plot(θ1_lin, Rp_func(np.deg2rad(θ1_lin)), label=r'$R_p$ teori')

# Udregn Brewsters vinkel og plot
θ_B = np.arctan(n_glas/n_luft)
plt.plot([np.rad2deg(θ_B), np.rad2deg(θ_B)], [0.0, 0.05], color='r', linestyle='--', label='Brewster Angle')

# Plot settings
plt.xlim(20, 90)
plt.ylim(0, 1.3)
plt.xlabel(r'Incident Angle $(θ_1)$')
plt.ylabel('Reflectance')
plt.title('Reflectance vs Incident Angle')
plt.legend(fontsize=12)
plt.show()