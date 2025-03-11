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
    return np.arcsin(n_glas / n_luft * np.sin(θ1))

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
    return np.rad2deg(np.arctan(n2/n1))

def critical(n): 
    return np.rad2deg(np.arcsin(1/n))

baggrund = 0.0366   # Background intensity
n_glas = 1.5        # Teoretical glass index
n_luft = 1.0        # Air index

# Messured angle of small disk 
θ1_list = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 42, 43, 44, 45,50,55,60])

# Messured angle of Transmission, rewritten from 180 -> 0 to 0 -> 180
φ2_list = np.array([172, 169.5, 166, 162.2, 158, 151, 146, 142.2, 135.2])
φ2_list = 180 - φ2_list

# Calculated θ2
θ2_list = θ1_list[3:-4] + φ2_list

# Messured angle of Reflection 
φ1_list = np.array([26.5, 36.5, 47, 58, 66.5, 76.2, 80.9, 82.9, 84.2, 86.7, 97, 107, 112])

θ1_lin = np.linspace(1, 90, 1000)

# Calculated index of glass from experiment
n_g_list = np.sin(np.deg2rad(θ2_list)) / np.sin(np.deg2rad(θ1_list[3:-4]))
n_g_teori = np.average(n_g_list)

print(f'n_glas_teori = {n_g_teori}')


# Transmittet intensities 
T_s = np.array([2.464, 2.114, 2.008, 1.785, 2.332, 1.429, 2.262, 1.988, 2.383, 1.992, 1.722, 0.632]) - baggrund
T_p = np.array([2.297, 2.692, 1.944, 1.848, 2.181, 1.329, 1.973, 1.682, 1.862, 1.397, 1.108, 0.333]) - baggrund

# Reflekteret intensities
R_s = np.array([0.085, 0.073, 0.054, 0.047, 0.030, 0.055, 0.177, 0.370, 1.109, 1.757, 1.747, 2.198, 1.841]) - baggrund
R_p = np.array([0.114, 0.117, 0.127, 0.233, 0.239, 0.450, 0.623, 0.912, 1.530, 2.088, 2.011, 1.972, 2.252]) - baggrund

# Normalize Intensities 
R_s = R_s/T_s[0]
R_p = R_p/T_p[0]

T_s = T_s/T_s[0]
T_p = T_p/T_p[0]


# Fit functions to data
popt_Rs, Rs_pcov = curve_fit(Rs_func, np.deg2rad(θ1_list[3:-3]), R_s[:-3], p0=[1.2])
popt_Rp, Rp_pcov = curve_fit(Rp_func, np.deg2rad(θ1_list[3:-3]), R_p[:-3], p0=[1.2])
popt_Ts, Ts_pcov = curve_fit(Ts_func, np.deg2rad(θ1_list[1:-4]), T_s[1:], p0=[1.2])
popt_Tp, Tp_pcov = curve_fit(Tp_func, np.deg2rad(θ1_list[1:-4]), T_p[1:], p0=[1.2])

# Plot reflected as function of insidentangle
plt.errorbar(θ1_list[3:-3], R_s[:-3], yerr=0.01, fmt=".", capsize=5, label=r'$R_s$')
plt.errorbar(θ1_list[3:-3], R_p[:-3], yerr=0.01, fmt=".", capsize=5, label=r'$R_p$')

# Plot teori
plt.plot(θ1_lin, Rs_func(np.deg2rad(θ1_lin), n_glas), label=r'$R_s$ theory')
plt.plot(θ1_lin, Rp_func(np.deg2rad(θ1_lin), n_glas), label=r'$R_p$ theory')

# Plot the fits
plt.plot(θ1_lin, Rp_func(np.deg2rad(θ1_lin), *popt_Rp), "--", label='Fit $R_p$')
plt.plot(θ1_lin, Rs_func(np.deg2rad(θ1_lin), *popt_Rs), "--", label='Fit $R_s$')

# Print the variables from the curve fit
print(f'Fit parameters for Rs: {popt_Rs}, error: {np.sqrt(np.diag(Rs_pcov))}')
print(f'Fit parameters for Rp: {popt_Rp}, error: {np.sqrt(np.diag(Rp_pcov))}')

# Assuming popt_Rs and popt_Rp contain the fitted refractive indices (n_2)
n2_Rs = popt_Rs[0]  # Fitted value
n2_Rp = popt_Rp[0]  # Fitted value

# Extract uncertainties from covariance matrix
sigma_n2_Rs = np.sqrt(np.diag(Rs_pcov))[0]  # Standard deviation of fit parameter
sigma_n2_Rp = np.sqrt(np.diag(Rp_pcov))[0]  # Standard deviation of fit parameter

# Brewster's angle: θ_B = arctan(n2/n1), assuming n1 = 1 (air)
theta_B_Rs = np.rad2deg(np.arctan(1/n2_Rs))
theta_B_Rp = np.rad2deg(np.arctan(1/n2_Rp))

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
theta_B_Ts = np.rad2deg(np.arctan(1/n2_Ts))
theta_B_Tp = np.rad2deg(np.arctan(1/n2_Tp))

# Propagate uncertainty for Brewster’s angle
sigma_theta_B_Ts = np.rad2deg((1 / (1 + n2_Ts**2)) * (sigma_n2_Ts))
sigma_theta_B_Tp = np.rad2deg((1 / (1 + n2_Tp**2)) * (sigma_n2_Tp))

# Critical angle: θ_C = arcsin(1/n2)
theta_C_Ts = np.rad2deg(np.arcsin(1/n2_Ts))
theta_C_Tp = np.rad2deg(np.arcsin(1/n2_Tp))

# Propagate uncertainty for critical angle
sigma_theta_C_Ts = np.rad2deg((1 / np.sqrt(1 - (1/n2_Ts)**2)) * (sigma_n2_Ts / n2_Ts**2))
sigma_theta_C_Tp = np.rad2deg((1 / np.sqrt(1 - (1/n2_Tp)**2)) * (sigma_n2_Tp / n2_Tp**2))

# Print results with correct uncertainty
print(f"Brewster angle from fit (T_s): {theta_B_Ts:.2f} ± {sigma_theta_B_Ts:.2f} degrees")
print(f"Brewster angle from fit (T_p): {theta_B_Tp:.2f} ± {sigma_theta_B_Tp:.2f} degrees")

print(f"Critical angle from fit (T_s): {theta_C_Ts:.2f} ± {sigma_theta_C_Ts:.2f} degrees")
print(f"Critical angle from fit (T_p): {theta_C_Tp:.2f} ± {sigma_theta_C_Tp:.2f} degrees")

# Calculate Brewster angle and plot
θ_B = brewster(n_g_teori,1)
print(f"Brewster angle = {θ_B}")
plt.plot([θ_B, θ_B], [0.0, 0.05], color='r', linestyle='--', label='Brewster Angle')

# Calculate critical angle and plot
θ_C = critical(n_g_teori)
print(f"Critical angle = {θ_C}")
plt.plot([θ_C, θ_C], [0.0, 0.05], color='b', linestyle='--', label='Critical Angle')

# Plot settings
plt.xlim(0, 60)
plt.ylim(0, 1.3)
plt.xlabel(r'Incident Angle $(θ_1)$')
plt.ylabel('Reflectance (V)')
plt.title('Reflectance vs Incident Angle')
plt.legend(fontsize=12)
plt.show()

# Plot Transmittet as function of insident angle
plt.errorbar(θ1_list[:-4], T_s, yerr=0.01, fmt=".", capsize=5, label=r'$T_s$')
plt.errorbar(θ1_list[:-4], T_p, yerr=0.01, fmt=".", capsize=5, label=r'$T_p$')

# Plot teori
plt.plot(θ1_lin, Ts_func(np.deg2rad(θ1_lin), n_glas), label=r'$T_s$ theory')
plt.plot(θ1_lin, Tp_func(np.deg2rad(θ1_lin), n_glas), label=r'$T_p$ theory')

# Fits 
plt.plot(θ1_lin, Tp_func(np.deg2rad(θ1_lin), *popt_Tp), "--", label='Fit $T_p$')
plt.plot(θ1_lin, Ts_func(np.deg2rad(θ1_lin), *popt_Ts), "--", label='Fit $T_s$')

print(f'Fit parameters for Ts: {popt_Ts}, error: {np.sqrt(np.diag(Ts_pcov))}')
print(f'Fit parameters for Tp: {popt_Tp}, error: {np.sqrt(np.diag(Tp_pcov))}')


# Plot settings
plt.xlim(0, 60)
plt.ylim(0, 1.3)
plt.xlabel(r'Incident Angle $(θ_1)$')
plt.ylabel('Transmission (V)')
plt.title('Transmission vs Incident Angle')
plt.legend(fontsize=12)
plt.show()

print(T_s[3:]+R_s[:-4])
print(T_p[3:]+R_p[:-4])

# Calculate chi^2 for all fits
def chi_squared(observed, expected, errors):
    return np.sum(((observed - expected) / errors) ** 2)

# Calculate errors (assuming Poisson statistics for simplicity)
errors_Rs = np.sqrt(R_s)
errors_Rp = np.sqrt(R_p)
errors_Ts = np.sqrt(T_s)
errors_Tp = np.sqrt(T_p)

# Calculate expected values from the fit parameters
expected_Rs = Rs_func(np.deg2rad(θ1_list[3:-3]), *popt_Rs)
expected_Rp = Rp_func(np.deg2rad(θ1_list[3:-3]), *popt_Rp)
expected_Ts = Ts_func(np.deg2rad(θ1_list[1:-4]), *popt_Ts)
expected_Tp = Tp_func(np.deg2rad(θ1_list[1:-4]), *popt_Tp)

# Calculate chi^2 for each fit
chi2_Rs = chi_squared(R_s[:-3], expected_Rs, errors_Rs[:-3])
chi2_Rp = chi_squared(R_p[:-3], expected_Rp, errors_Rp[:-3])
chi2_Ts = chi_squared(T_s[1:], expected_Ts, errors_Ts[1:])
chi2_Tp = chi_squared(T_p[1:], expected_Tp, errors_Tp[1:])

# Print chi^2 values
print(f'Chi^2 for Rs fit: {chi2_Rs}')
print(f'Chi^2 for Rp fit: {chi2_Rp}')
print(f'Chi^2 for Ts fit: {chi2_Ts}')
print(f'Chi^2 for Tp fit: {chi2_Tp}')

# Average Brewster angles and their uncertainties
brewster_angles = [theta_B_Rs, theta_B_Rp, theta_B_Ts, theta_B_Tp]
brewster_uncertainties = [sigma_theta_B_Rs, sigma_theta_B_Rp, sigma_theta_B_Ts, sigma_theta_B_Tp]

average_brewster_angle = np.mean(brewster_angles)
average_brewster_uncertainty = np.sqrt(np.sum(np.array(brewster_uncertainties)**2)) / len(brewster_uncertainties)

print(f"Average Brewster angle: {average_brewster_angle:.2f} ± {average_brewster_uncertainty:.2f} degrees")

# Average critical angles and their uncertainties
critical_angles = [theta_C_Rs, theta_C_Rp, theta_C_Ts, theta_C_Tp]
critical_uncertainties = [sigma_theta_C_Rs, sigma_theta_C_Rp, sigma_theta_C_Ts, sigma_theta_C_Tp]

average_critical_angle = np.mean(critical_angles)
average_critical_uncertainty = np.sqrt(np.sum(np.array(critical_uncertainties)**2)) / len(critical_uncertainties)

print(f"Average critical angle: {average_critical_angle:.2f} ± {average_critical_uncertainty:.2f} degrees")

print(f"{brewster(1.5, 1)}")
print(f"{critical(1.5)}")