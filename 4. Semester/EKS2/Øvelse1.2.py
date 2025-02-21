# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Plot settings
plt.rc("axes", labelsize=18, titlesize=22)   # skriftstørrelse af `xlabel`, `ylabel` og `title`
plt.rc("xtick", labelsize=16, top=True, direction="in")  # skriftstørrelse af ticks, vis også ticks øverst og vend ticks indad
plt.rc("ytick", labelsize=16, right=True, direction="in") # samme som ovenstående
plt.rc("legend", fontsize=16) # skriftstørrelse af figurers legends

# Functioner 
def find_θ2(θ1, n_glas):
    return np.arcsin(n_luft / n_glas * np.sin(θ1))

def Rs_func(θ1, n_glas): 
    θ2 = find_θ2(θ1, n_glas)
    return np.sin(θ1 - θ2)**2 / np.sin(θ1 + θ2)**2

def Rp_func(θ1, n_glas):
    θ2 = find_θ2(θ1, n_glas)
    return np.tan(θ1 - θ2)**2 / np.tan(θ1 + θ2)**2

def Ts_func(θ1, n_glas):
    θ2 = find_θ2(θ1, n_glas)
    return np.sin(2*θ1) * np.sin(2*θ2) / np.sin(θ1 + θ2)**2

def Tp_func(θ1, n_glas):
    θ2 = find_θ2(θ1, n_glas)
    return np.sin(2*θ1) * np.sin(2*θ2) / (np.sin(θ1 + θ2)**2 * np.cos(θ1 - θ2)**2)

baggrund = 0.0366   # Background intensity
n_glas = 1.5        # Teoretical glass index
n_luft = 1.0        # Air index

# Messured angle of small disk 
θ1_list = np.array([15, 20, 25, 30,35,40,45,50,55,60,65,70,75,80,85])

# Messured angle of Transmission, rewritten from 180 -> 0 to 0 -> 180
φ2_list = np.array([176, 174,172,171,172,174,176,178,161,164,167,151,155,141,145])
φ2_list = 180 - φ2_list

# Calculated θ2
θ2_list = θ1_list - φ2_list

# Messured angle of Reflection 
θ1_lin = np.linspace(1, 90, 1000)

# Calculated index of glass from experiment
n_g_list = np.sin(np.deg2rad(θ1_list)) / np.sin(np.deg2rad(θ2_list))
n_g_teori = np.average(n_g_list)

print(f'n_glas_teori = {n_g_teori}')


# Transmittet intensities 
T_s = np.array([4.98, 5.13, 5.18, 5.16, 5.17, 4.92, 5.11, 4.805, 4.437, 4.429, 4.541, 3.842, 3.400, 2.744, 1.599, 0.472]) - baggrund
T_p = np.array([4.88, 4.37, 4.52, 4.48, 4.64, 4.07, 4.45, 4.411, 4.19, 4.15, 4.539, 4.059, 3.825, 3.303, 2.198, 0.715]) - baggrund

# Reflekteret intensities
R_s = np.array([0.207, 0.232, 0.282, 0.285, 0.343, 0.48, 0.477, 0.604, 0.878, 1.136, 1.456, 2.268, 3.216, 4.638]) - baggrund
R_p = np.array([0.159, 0.146, 0.122, 0.096, 0.09, 0.066, 0.017, 0.004, 0.005, 0.0064, 0.166, 0.444, 1.040, 2.339]) - baggrund

# Normalize Intensities 
R_s = R_s/T_s[0]
R_p = R_p/T_p[0]

T_s = T_s/T_s[0]
T_p = T_p/T_p[0]

# Fit functions to data
popt_Rs, Rs_pcov = curve_fit(Rs_func, np.deg2rad(θ1_list[1:]), R_s, p0=[1.2])
popt_Rp, Rp_pcov = curve_fit(Rp_func, np.deg2rad(θ1_list[1:]), R_p, p0=[1.5])
popt_Ts, Ts_pcov = curve_fit(Ts_func, np.deg2rad(θ1_list[:]), T_s[1:], p0=[1.5])
popt_Tp, Tp_pcov = curve_fit(Tp_func, np.deg2rad(θ1_list[:]), T_p[1:], p0=[1])


# Plot reflected as function of insidentangle
plt.plot(θ1_list[1:], R_s, "o", label=r'$R_s$')
plt.plot(θ1_list[1:], R_p, "o",  label=r'$R_p$')

# Plot teori
plt.plot(θ1_lin, Rs_func(np.deg2rad(θ1_lin), n_glas), label=r'$R_s$ theory')
plt.plot(θ1_lin, Rp_func(np.deg2rad(θ1_lin), n_glas), label=r'$R_p$ theory')

# Plot the fits
plt.plot(θ1_lin, Rp_func(np.deg2rad(θ1_lin), *popt_Rp), "--", label='Fit $R_p$')
plt.plot(θ1_lin, Rs_func(np.deg2rad(θ1_lin), *popt_Rs), "--", label='Fit $R_s$')

# Print the variables from the curve fit
print(f'Fit parameters for Rs: {popt_Rs}, error: {np.sqrt(np.diag(Rs_pcov))}')
print(f'Fit parameters for Rp: {popt_Rp}, error: {np.sqrt(np.diag(Rp_pcov))}')


# Calculate Brewster angle and plot
θ_B = np.arctan(n_glas/n_luft)
plt.plot([np.rad2deg(θ_B), np.rad2deg(θ_B)], [0.0, 0.05], color='r', linestyle='--', label='Brewster Angle')

# Plot settings
plt.xlim(10, 90)
plt.ylim(0, 1.3)
plt.xlabel(r'Incident Angle $(θ_1)$')
plt.ylabel('Reflectance (V)')
plt.title('Reflectance vs Incident Angle')
plt.legend(fontsize=12)
plt.show()

# Plot Transmittet as function of insident angle
plt.plot(θ1_list[:], T_s[1:], "o", label=r'$T_s$')
plt.plot(θ1_list[:], T_p[1:], "o",  label=r'$T_p$')

# Plot teori
plt.plot(θ1_lin, Ts_func(np.deg2rad(θ1_lin), n_glas), label=r'$T_s$ theory')
plt.plot(θ1_lin, Tp_func(np.deg2rad(θ1_lin), n_glas), label=r'$T_p$ theory')

# Fits 
plt.plot(θ1_lin, Tp_func(np.deg2rad(θ1_lin), *popt_Tp), "--", label='Fit $T_p$')
plt.plot(θ1_lin, Ts_func(np.deg2rad(θ1_lin), *popt_Ts), "--", label='Fit $T_s$')

print(f'Fit parameters for Ts: {popt_Ts}, error: {np.sqrt(np.diag(Ts_pcov))}')
print(f'Fit parameters for Tp: {popt_Tp}, error: {np.sqrt(np.diag(Tp_pcov))}')

# Plot settings
plt.xlim(0, 90)
plt.ylim(0, 1.3)
plt.xlabel(r'Incident Angle $(θ_1)$')
plt.ylabel('Transmission (V)')
plt.title('Transmission vs Incident Angle')
plt.legend(fontsize=12)
plt.show()

print(T_s[2:]+R_s)
print(T_p[2:]+R_p)