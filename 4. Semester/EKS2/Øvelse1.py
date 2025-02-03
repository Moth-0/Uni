# Imports
import numpy as np
import matplotlib.pyplot as plt

# Plot settings
plt.rc("axes", labelsize=18, titlesize=22)   # skriftstørrelse af `xlabel`, `ylabel` og `title`
plt.rc("xtick", labelsize=16, top=True, direction="in")  # skriftstørrelse af ticks, vis også ticks øverst og vend ticks indad
plt.rc("ytick", labelsize=16, right=True, direction="in") # samme som ovenstående
plt.rc("legend", fontsize=16) # skriftstørrelse af figurers legends

# Brydningsindex
# n_{glas} = n_{luft} * sin(θ_1) / sin(θ_2)

θ1_list = np.array([20, 35, 40, 55, 70, 85])

φ2_list = np.array([7.5, 13, 15, 23, 33, -1])
θ2_list = θ1_list - φ2_list

n_luft = 1 

n_glas = np.sin(np.average(np.deg2rad(θ1_list))) / np.sin(np.average(np.deg2rad(θ2_list)))

print(n_glas)

#%% 
# Intensistet 

# Transmittet
T_s = np.array([1.02, 1.61, 1.22, 1.43, 0.92, 0.19])
T_p = np.array([1.01, 1.68, 1.27, 1.65, 1.35, 0.19])

# Reflekteret
R_s = np.array([0.01, 0.01, 0.14, 0.24, 0.51, 1.11])
R_p = np.array([0.07, 0.05, 0.05, 0.04, 0.13, 0.88])

# Plot reflekteret som funktion af indfaldsvinkel
plt.plot(θ1_list, R_s, label=r'$R_s$')
plt.plot(θ1_list, R_p, label=r'$R_p$')

# Udregn Brewsters vinkel og plot
θ_B = np.arctan(n_glas/n_luft)
plt.plot([np.rad2deg(θ_B), np.rad2deg(θ_B)], [0.0, 0.05], color='r', linestyle='--', label='Brewster Angle')

# Critical angle (kun for n1 > n2, så glas -> luft)
#θ_C = np.arcsin(1/1.5)
#plt.plot([np.rad2deg(θ_C), np.rad2deg(θ_C)], [0.0, 0.05], color='b', linestyle='--')

# Plot settings
plt.xlim(20, 90)
plt.ylim(0, 1)
plt.xlabel(r'Incident Angle $(θ_1)$')
plt.ylabel('Reflectance')
plt.title('Reflectance vs Incident Angle')
plt.legend()
plt.show()