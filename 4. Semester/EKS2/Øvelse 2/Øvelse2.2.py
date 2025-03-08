# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
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

def lin_func(x, a, b):
    return a * x + b

def Δs(max, v): 
    return 2 * laser_wavelength / v * max # IS THE 2 HERE RIGHT? 

def guess(a, b): 
    A = (np.max(b) - np.min(b))/2
    # Improved guess for B using the frequency of the data points
    peaks = find_peaks(b, height = 0, distance=100)[0]
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
v_max_list = []
c_inc = []
c_dec = []

# Folder containing the data files
folder = "dag2"

# Loop through each file in the folder
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    data = np.loadtxt(file_path, skiprows=3)

    freq, A, B = data.T

    A = A * 20 # From Amplicator 
    B = B * 0.001 # From mV to V

    # Find the midpoint where A is maximum
    mid = np.argmax(A)
    # Find the index where A goes over 0 and where it goes back under
    start = 50 + np.where(A[:mid] > 0)[0][0]
    end = mid + np.where(A[mid:] < 0)[0][0]

    # Split the data into two halves
    A1, B1 = A[start:mid], B[start:mid]  # First half (increasing V)
    A2, B2 = A[mid:end], B[mid:end]  # Second half (decreasing V)

    # Initial guesses for the sine function parameters
    initial_guess1 = guess(A1, B1)
    initial_guess2 = guess(A2, B2)


    # Fit sine function to both halves
    popt1, _ = curve_fit(sine_func, A1, B1, p0=initial_guess1, maxfev=10000)
    popt2, _ = curve_fit(sine_func, A2, B2, p0=initial_guess2, maxfev=10000)

    # Calculate the wavelength from the fit parameters
    lambda_V1 = abs(popt1[1])
    lambda_V2 = abs(popt2[1])

    # Compute the piezoelectric constant C for both cases
    C1 = laser_wavelength / (2 * lambda_V1) # m / V
    C2 = laser_wavelength / (2 * lambda_V2)
    
    # Average the two values of C
    C_avg = (C1 + C2) / 2

    # Store results
    v_inc_list.append(lambda_V1)  # Store ΔV for increasing V
    v_dec_list.append(lambda_V2)  # Store ΔV for decreasing V
    v_max_list.append(A[mid])  # Store V_max
    c_inc.append(C1)  # Store computed C for increasing V
    c_dec.append(C2)  # Store computed C for decreasing V


    if plots: 
        print(f"ΔV (Increasing): {lambda_V1:.5f} V")
        print(f"ΔV (Decreasing): {lambda_V2:.5f} V")

        print(f"C (Increasing): {C1:.5e} m/V")
        print(f"C (Decreasing): {C2:.5e} m/V")
        print(f"C (Average): {C_avg:.5e} m/V")
        
        # Plot the data and the fits
        plt.plot(A1, B1, label='First Half')
        plt.plot(A2, B2, label='Second Half')
        plt.plot(A1, sine_func(A1, *popt1), '--', label='Fit First Half')
        plt.plot(A2, sine_func(A2, *popt2), '--', label='Fit Second Half')

        # Plot settings
        plt.xlabel('A (V)')
        plt.ylabel('B (V)')
        plt.title(r'Wave Analysis $V_{max}=$' + f"{A[mid]:.1f} V")
        plt.legend()
        plt.show()


# Convert to NumPy arrays for easier analysis
v_inc_list = np.array(v_inc_list)
v_dec_list = np.array(v_dec_list)
v_max_list = np.array(v_max_list)
c_inc = np.array(c_inc)
c_dec = np.array(c_dec)

v_lin = np.linspace(0, 150)

# Plot C vs. V_max
plt.figure(figsize=(8,6))
plt.scatter(v_max_list, c_inc, color='blue', label=r"$C_{increasing}$")
plt.scatter(v_max_list, c_dec, color='red', label=r"$C_{decreasing}$")
plt.xlabel(r"$V_{max}$ (V)")
plt.ylabel(r"Piezoelectric Constant $C$ (μm/V)")
plt.title("Variation of Piezoelectric Constant with $V_{max}$")
plt.legend()
plt.show()

# Calculate Δs
Δs_inc = Δs(v_max_list, v_inc_list) * 10**6 # m to μm
Δs_dec = Δs(v_max_list, v_dec_list) * 10**6 

# Linear fit for Δs vs. V_max
popt_inc, _ = curve_fit(lin_func, v_max_list, Δs_inc)
popt_dec, _ = curve_fit(lin_func, v_max_list, Δs_dec)

# Plot Δs vs. V_max with linear fit
plt.figure(figsize=(8,6))
plt.plot(v_max_list, Δs_inc, "o", label="Increasing")
plt.plot(v_max_list, Δs_dec, "o", label="Decreasing")
plt.plot(v_lin, lin_func(v_lin, *popt_inc), '--', label="Fit Increasing")
plt.plot(v_lin, lin_func(v_lin, *popt_dec), '--', label="Fit Decreasing")
plt.xlabel(r"$V_{max}$ (V)")
plt.ylabel(r"$\Delta s$ (μm)")
plt.title(r"Variation of $\Delta s$ with $V_{max}$")
plt.legend()
plt.show()

# Print Summary Statistics
print("\nFinal Summary:")
print(f"C increasing from fit: {popt_inc[0]:.5e} μm/V - b value {popt_inc[1]}")
print(f"C decreasing from fit: {popt_dec[0]:.5e} μm/V - b value {popt_dec[1]}")