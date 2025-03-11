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

# Error for error bars
error = 0.01

# Plot reflected as function of insidentangle
plt.errorbar(θ1_list[1:], R_s, yerr=error, fmt=".", capsize=5, label=r'$R_s$')
plt.errorbar(θ1_list[1:], R_p, yerr=error, fmt=".", capsize=5, label=r'$R_p$')

# Plot teori
plt.plot(θ1_lin, Rs_func(np.deg2rad(θ1_lin), n_glas), label=r'$R_s$ theory')
plt.plot(θ1_lin, Rp_func(np.deg2rad(θ1_lin), n_glas), label=r'$R_p$ theory')

# Plot the fits
plt.plot(θ1_lin, Rp_func(np.deg2rad(θ1_lin), *popt_Rp), "--", label='Fit $R_p$')
plt.plot(θ1_lin, Rs_func(np.deg2rad(θ1_lin), *popt_Rs), "--", label='Fit $R_s$')

# Print the variables from the curve fit
print(f'Fit parameters for Rs: {popt_Rs}, error: {np.sqrt(np.diag(Rs_pcov))}')
print(f'Fit parameters for Rp: {popt_Rp}, error: {np.sqrt(np.diag(Rp_pcov))}')
print(f"Brewster angle from fit: {np.rad2deg(np.arctan(popt_Rs))} pm {np.rad2deg(np.arctan(np.sqrt(np.diag(Rs_pcov))))}")
print(f"Brewster angle from fit: {np.rad2deg(np.arctan(popt_Rp))} pm {np.rad2deg(np.arctan(np.sqrt(np.diag(Rp_pcov))))}")

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
plt.errorbar(θ1_list[:], T_s[1:], yerr=error, fmt=".", capsize=5, label=r'$T_s$')
plt.errorbar(θ1_list[:], T_p[1:], yerr=error, fmt=".", capsize=5, label=r'$T_p$')

# Plot teori
plt.plot(θ1_lin, Ts_func(np.deg2rad(θ1_lin), n_glas), label=r'$T_s$ theory')
plt.plot(θ1_lin, Tp_func(np.deg2rad(θ1_lin), n_glas), label=r'$T_p$ theory')

# Fits 
plt.plot(θ1_lin, Tp_func(np.deg2rad(θ1_lin), *popt_Tp), "--", label='Fit $T_p$')
plt.plot(θ1_lin, Ts_func(np.deg2rad(θ1_lin), *popt_Ts), "--", label='Fit $T_s$')



print(f'Fit parameters for Ts: {popt_Ts}, error: {np.sqrt(np.diag(Ts_pcov))}')
print(f'Fit parameters for Tp: {popt_Tp}, error: {np.sqrt(np.diag(Tp_pcov))}')
print(f"Brewster angle from fit: {np.rad2deg(np.arctan(popt_Ts))} pm {np.rad2deg(np.arctan(np.sqrt(np.diag(Ts_pcov))))}")
print(f"Brewster angle from fit: {np.rad2deg(np.arctan(popt_Tp))} pm {np.rad2deg(np.arctan(np.sqrt(np.diag(Tp_pcov))))}")

# Assuming popt_Rs and popt_Rp contain the fitted refractive indices (n_2)
n2_Rs = popt_Rs[0]  # Fitted value
n2_Rp = popt_Rp[0]  # Fitted value

# Extract uncertainties from covariance matrix
sigma_n2_Rs = np.sqrt(np.diag(Rs_pcov))[0]  # Standard deviation of fit parameter
sigma_n2_Rp = np.sqrt(np.diag(Rp_pcov))[0]  # Standard deviation of fit parameter

# Brewster's angle: θ_B = arctan(n2/n1), assuming n1 = 1 (air)
theta_B_Rs = np.rad2deg(np.arctan(n2_Rs))
theta_B_Rp = np.rad2deg(np.arctan(n2_Rp))

# Propagate uncertainty for Brewster’s angle
sigma_theta_B_Rs = np.rad2deg((1 / (1 + n2_Rs**2)) * (sigma_n2_Rs))
sigma_theta_B_Rp = np.rad2deg((1 / (1 + n2_Rp**2)) * (sigma_n2_Rp))

# Critical angle: θ_C = arcsin(1/n2)
theta_C_Rs = np.rad2deg(np.arcsin(1 / n2_Rs))
theta_C_Rp = np.rad2deg(np.arcsin(1 / n2_Rp))

# Propagate uncertainty for critical angle
sigma_theta_C_Rs = np.rad2deg((1 / np.sqrt(1 - (1/n2_Rs)**2)) * (sigma_n2_Rs / n2_Rs**2))
sigma_theta_C_Rp = np.rad2deg((1 / np.sqrt(1 - (1/n2_Rp)**2)) * (sigma_n2_Rp / n2_Rp**2))

# Print results with correct uncertainty
print(f"Brewster angle from fit (R_s): {theta_B_Rs:.2f} ± {sigma_theta_B_Rs:.2f} degrees")
print(f"Brewster angle from fit (R_p): {theta_B_Rp:.2f} ± {sigma_theta_B_Rp:.2f} degrees")

print(f"Critical angle from fit (R_s): {theta_C_Rs:.2f} ± {sigma_theta_C_Rs:.2f} degrees")
print(f"Critical angle from fit (R_p): {theta_C_Rp:.2f} ± {sigma_theta_C_Rp:.2f} degrees")

# Assuming popt_Ts and popt_Tp contain the fitted refractive indices (n_2)
n2_Ts = popt_Ts[0]  # Fitted value
n2_Tp = popt_Tp[0]  # Fitted value

# Extract uncertainties from covariance matrix
sigma_n2_Ts = np.sqrt(np.diag(Ts_pcov))[0]  # Standard deviation of fit parameter
sigma_n2_Tp = np.sqrt(np.diag(Tp_pcov))[0]  # Standard deviation of fit parameter

# Brewster's angle: θ_B = arctan(n2/n1), assuming n1 = 1 (air)
theta_B_Ts = np.rad2deg(np.arctan(n2_Ts))
theta_B_Tp = np.rad2deg(np.arctan(n2_Tp))

# Propagate uncertainty for Brewster’s angle
sigma_theta_B_Ts = np.rad2deg((1 / (1 + n2_Ts**2)) * (sigma_n2_Ts))
sigma_theta_B_Tp = np.rad2deg((1 / (1 + n2_Tp**2)) * (sigma_n2_Tp))

# Critical angle: θ_C = arcsin(1/n2)
theta_C_Ts = np.rad2deg(np.arcsin(1 / n2_Ts))
theta_C_Tp = np.rad2deg(np.arcsin(1 / n2_Tp))

# Propagate uncertainty for critical angle
sigma_theta_C_Ts = np.rad2deg((1 / np.sqrt(1 - (1/n2_Ts)**2)) * (sigma_n2_Ts / n2_Ts**2))
sigma_theta_C_Tp = np.rad2deg((1 / np.sqrt(1 - (1/n2_Tp)**2)) * (sigma_n2_Tp / n2_Tp**2))

# Print results with correct uncertainty
print(f"Brewster angle from fit (T_s): {theta_B_Ts:.2f} ± {sigma_theta_B_Ts:.2f} degrees")
print(f"Brewster angle from fit (T_p): {theta_B_Tp:.2f} ± {sigma_theta_B_Tp:.2f} degrees")

print(f"Critical angle from fit (T_s): {theta_C_Ts:.2f} ± {sigma_theta_C_Ts:.2f} degrees")
print(f"Critical angle from fit (T_p): {theta_C_Tp:.2f} ± {sigma_theta_C_Tp:.2f} degrees")

print(T_s[2:]+R_s)
print(T_p[2:]+R_p)

# Calculate chi-squared for Rs
observed_Rs = R_s
expected_Rs = Rs_func(np.deg2rad(θ1_list[1:]), *popt_Rs)
chi_squared_Rs = np.sum(((observed_Rs - expected_Rs) ** 2) / expected_Rs)

# Calculate chi-squared for Rp
observed_Rp = R_p
expected_Rp = Rp_func(np.deg2rad(θ1_list[1:]), *popt_Rp)
chi_squared_Rp = np.sum(((observed_Rp - expected_Rp) ** 2) / expected_Rp)

# Calculate chi-squared for Ts
observed_Ts = T_s[1:]
expected_Ts = Ts_func(np.deg2rad(θ1_list[:]), *popt_Ts)
chi_squared_Ts = np.sum(((observed_Ts - expected_Ts) ** 2) / expected_Ts)

# Calculate chi-squared for Tp
observed_Tp = T_p[1:]
expected_Tp = Tp_func(np.deg2rad(θ1_list[:]), *popt_Tp)
chi_squared_Tp = np.sum(((observed_Tp - expected_Tp) ** 2) / expected_Tp)

print(f'Chi-squared for Rs: {chi_squared_Rs}')
print(f'Chi-squared for Rp: {chi_squared_Rp}')
print(f'Chi-squared for Ts: {chi_squared_Ts}')
print(f'Chi-squared for Tp: {chi_squared_Tp}')