# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
from scipy.stats import chi2
import os

# Plot settings
plt.rc("axes", labelsize=18, titlesize=22)
plt.rc("xtick", labelsize=16, top=True, direction="in")
plt.rc("ytick", labelsize=16, right=True, direction="in")
plt.rc("legend", fontsize=16)

print("\n\n\n-------------------------------")
plots = False

# Sine function for fitting
def sine_func(x, A, λ, φ, D):
    return A * np.sin(2*np.pi / λ * x + φ) + D

def lin_func(x, k):
    return k * x

def Δs(max, v): 
    return laser_wavelength / v * max  

def guess(a, b): 
    A = (np.max(b) - np.min(b))/2
    
    # Improved guess for B using the frequency of the data points
    peaks = find_peaks(b, height=0, distance=distance)[0]
    if len(peaks) > 1:
        avg_peak_distance = np.mean(np.diff(a[peaks]))
        B = avg_peak_distance
    else:
        B = a[-1] - a[0]
    
    C = 0
    D = np.mean(b)
    return [A, B, C, D]

# Constants
laser_wavelength = 632.8e-9  # meters (for HeNe laser)

# Lists to store results
v_inc_list = []
v_dec_list = []
v_inc_err = []
v_dec_err = []
v_max_list = []

# Folder containing the data files
folder = "dag3"

# Loop through each file in the folder
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    data = np.loadtxt(file_path, skiprows=3)

    freq, A, B = data.T

    A = A * 10 # From Amplicator 
    B = B * 0.001 # From mV to V

    # Find the midpoint where A is maximum
    mid = np.argmax(A)

    # Find the index where A goes over 0 and where it goes back under
    start = 30 + np.where(A[:mid] > 0)[0][0]
    end = mid + np.where(A[mid:] < 0)[0][0] - 20

    # Split the data into two halves
    A1, B1 = A[start:mid], B[start:mid]  # First half (increasing V)
    A2, B2 = A[mid:end], B[mid:end]  # Second half (decreasing V)

    distance = int(50 * (90 / A[mid]))

    # Initial guesses for the sine function parameters
    initial_guess1 = guess(A1, B1)
    initial_guess2 = guess(A2, B2)


    # Fit sine function to both halves
    sigma1 = np.full_like(B1, 0.1)
    sigma2 = np.full_like(B2, 0.1)
    popt1, err1 = curve_fit(sine_func, A1, B1, p0=initial_guess1, maxfev=10000, sigma=sigma1, absolute_sigma=False)
    popt2, err2 = curve_fit(sine_func, A2, B2, p0=initial_guess2, maxfev=10000, sigma=sigma2, absolute_sigma=False)

    
    # Calculate the wavelength from the fit parameters
    lambda_V1 = abs(popt1[1])
    lambda_V2 = abs(popt2[1])

    # Store results
    v_inc_list.append(lambda_V1)  # Store ΔV for increasing V
    v_dec_list.append(lambda_V2)  # Store ΔV for decreasing V

    # Calculate the error of the fit parameters
    perr1 = np.sqrt(np.diag(err1))[1]
    perr2 = np.sqrt(np.diag(err2))[1]
    

    # Store the errors
    v_inc_err.append(perr1)
    v_dec_err.append(perr2)
    
    v_max_list.append(A[mid])  # Store V_max

    if plots: 
        print(f"{str(file)}")
        print(f"ΔV (Increasing): {lambda_V1:.5f} V")
        print(f"ΔV (Decreasing): {lambda_V2:.5f} V")
        print(f"Inc_err: {perr1:.5f} V")
        print(f"Dec_err: {perr2:.5f} V")

        # Calculate chi-squared for the fits
        chi2_inc = np.sum(((B1 - sine_func(A1, *popt1)) / perr1) ** 2)
        chi2_dec = np.sum(((B2 - sine_func(A2, *popt2)) / perr2) ** 2)
        
        # Print chi-squared values
        print(f"Chi-squared (Increasing): {chi2_inc:.5f}")
        print(f"Chi-squared (Decreasing): {chi2_dec:.5f}")


        # Plot the data and the fits
        plt.plot(A1, B1, label='First Half')
        plt.plot(A2, B2, label='Second Half')
        plt.plot(A1, sine_func(A1, *popt1), '--', label='Fit First Half')
        plt.plot(A2, sine_func(A2, *popt2), '--', label='Fit Second Half')

        # Plot the peaks found with find_peaks
        peaks1 = find_peaks(B1, height=0, distance=distance)[0]
        peaks2 = find_peaks(B2, height=0, distance=distance)[0]
        plt.plot(A1[peaks1], B1[peaks1], 'x', label='Peaks First Half')
        plt.plot(A2[peaks2], B2[peaks2], 'x', label='Peaks Second Half')
        

        # Plot settings
        plt.xlabel('A (V)')
        plt.ylabel('B (V)')
        plt.title(r'Wave Analysis $V_{max}=$' + f"{A[mid]:.1f} V")
        plt.show()

        


# Convert to NumPy arrays for easier analysis
v_inc_list = np.array(v_inc_list)
v_dec_list = np.array(v_dec_list)
v_max_list = np.array(v_max_list)
v_inc_err = np.array(v_inc_err)
v_dec_err = np.array(v_dec_err)

v_lin = np.linspace(20, 95)

# Calculate Δs
Δs_inc = Δs(v_max_list, v_inc_list) * 10**6 # m to μm
Δs_dec = Δs(v_max_list, v_dec_list) * 10**6 

# Compute the propagated error using error propagation formula
Δs_inc_err = np.abs(- 2 * v_max_list * laser_wavelength / v_inc_list**2) * v_inc_err * 10**6  # Convert to μm
Δs_dec_err = np.abs(- 2 * v_max_list * laser_wavelength / v_dec_list**2) * v_dec_err * 10**6

# Linear fit for Δs vs. V_max
popt_inc, _ = curve_fit(lin_func, v_max_list, Δs_inc)
popt_dec, _ = curve_fit(lin_func, v_max_list, Δs_dec)

# Plot Δs vs. V_max with linear fit and error bars
plt.figure(figsize=(8,6))
plt.errorbar(v_max_list, Δs_inc, yerr=Δs_inc_err, fmt=".", label="Increasing", capsize=5)
plt.errorbar(v_max_list, Δs_dec, yerr=Δs_dec_err, fmt=".", label="Decreasing", capsize=5)
plt.plot(v_lin, lin_func(v_lin, *popt_inc), '--', label="Fit Increasing")
plt.plot(v_lin, lin_func(v_lin, *popt_dec), '--', label="Fit Decreasing")
plt.xlabel(r"$V_{max}$ (V)")
plt.ylabel(r"$\Delta s$ (μm)")
plt.title(r"Variation of $\Delta s$ with $V_{max}$")
plt.legend()
plt.show()

# Print Summary Statistics
print("\nFinal Summary:")
print(f"k increasing from fit: {popt_inc[0]:.5e} μm/V - value of Δl at 150V {popt_inc[0]*0.5*150:.3f} μm")
print(f"k decreasing from fit: {popt_dec[0]:.5e} μm/V - value of Δl at 150V {popt_dec[0]*0.5*150:.3f} μm")