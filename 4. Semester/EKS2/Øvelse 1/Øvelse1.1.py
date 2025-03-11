# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Plot settings
plt.rc("axes", labelsize=18, titlesize=22)
plt.rc("xtick", labelsize=16, top=True, direction="in")
plt.rc("ytick", labelsize=16, right=True, direction="in")
plt.rc("legend", fontsize=16)

# Constants
n_luft = 1.0  # Air index
n_glas_teori = 1.5  # Theoretical glass index
baggrund = 0.0366  # Background intensity

# Functions
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

def brewster(n1, n2):
    return np.rad2deg(np.arctan(n2 / n1))

def critical(n):
    return np.rad2deg(np.arcsin(1 / n))

# Data for Air-to-Glass
θ1_air_to_glass = np.array([15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
φ2_air_to_glass = 180 - np.array([176, 174, 172, 171, 172, 174, 176, 178, 161, 164, 167, 151, 155, 141, 145])
θ2_air_to_glass = θ1_air_to_glass - φ2_air_to_glass

# Data for Glass-to-Air
θ1_glass_to_air = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 42, 43, 44, 45, 50, 55, 60])
φ2_glass_to_air = 180 - np.array([172, 169.5, 166, 162.2, 158, 151, 146, 142.2, 135.2])
θ2_glass_to_air = θ1_glass_to_air[3:-4] + φ2_glass_to_air

# Function to process data
def process_experiment(θ1_list, θ2_list, label):
    # Measured intensities (background corrected)
    T_s = np.array([4.98, 5.13, 5.18, 5.16, 5.17, 4.92, 5.11, 4.805, 4.437, 4.429, 4.541, 3.842, 3.400, 2.744, 1.599, 0.472]) - baggrund
    T_p = np.array([4.88, 4.37, 4.52, 4.48, 4.64, 4.07, 4.45, 4.411, 4.19, 4.15, 4.539, 4.059, 3.825, 3.303, 2.198, 0.715]) - baggrund
    R_s = np.array([0.207, 0.232, 0.282, 0.285, 0.343, 0.48, 0.477, 0.604, 0.878, 1.136, 1.456, 2.268, 3.216, 4.638]) - baggrund
    R_p = np.array([0.159, 0.146, 0.122, 0.096, 0.09, 0.066, 0.017, 0.004, 0.005, 0.0064, 0.166, 0.444, 1.040, 2.339]) - baggrund

    # Normalize intensities
    R_s /= T_s[0]
    R_p /= T_p[0]
    T_s /= T_s[0]
    T_p /= T_p[0]

    # Curve fitting
    popt_Rs, Rs_pcov = curve_fit(Rs_func, np.deg2rad(θ1_list[1:]), R_s, p0=[1.2])
    popt_Rp, Rp_pcov = curve_fit(Rp_func, np.deg2rad(θ1_list[1:]), R_p, p0=[1.5])
    
    # Plot Reflectance
    plt.errorbar(θ1_list[1:], R_s, yerr=0.01, fmt=".", capsize=5, label=f'R_s {label}')
    plt.errorbar(θ1_list[1:], R_p, yerr=0.01, fmt=".", capsize=5, label=f'R_p {label}')
    θ1_lin = np.linspace(1, 90, 1000)
    plt.plot(θ1_lin, Rs_func(np.deg2rad(θ1_lin), n_glas_teori), label=f'R_s theory {label}')
    plt.plot(θ1_lin, Rp_func(np.deg2rad(θ1_lin), n_glas_teori), label=f'R_p theory {label}')
    plt.xlabel(r'Incident Angle $(\theta_1)$')
    plt.ylabel('Reflectance (V)')
    plt.title(f'Reflectance vs Incident Angle ({label})')
    plt.legend()
    plt.show()

# Process both experiments
process_experiment(θ1_air_to_glass, θ2_air_to_glass, "Air-to-Glass")
process_experiment(θ1_glass_to_air, θ2_glass_to_air, "Glass-to-Air")
