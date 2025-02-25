# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import os 

# Plot settings
plt.rc("axes", labelsize=18, titlesize=22)
plt.rc("xtick", labelsize=16, top=True, direction="in")
plt.rc("ytick", labelsize=16, right=True, direction="in")
plt.rc("legend", fontsize=16)

# Function to find peaks and lows in the data
def peaks(a, b): 
    peak = find_peaks(b, height=0, distance=100000)[0]
    low = find_peaks(-b, height=0, distance=100000)[0]
    
    plt.plot(a[peak], b[peak], "o")
    plt.plot(a[low], b[low], "o")

    return a[peak], a[low]

# Function to calculate the average wavelength from peaks and lows
def wave_len(peaks, lows):
    peak_distances = np.diff(peaks)
    low_distances = np.diff(lows)
    avg_wavelength = (np.mean(peak_distances) + np.mean(low_distances)) / 2
    return abs(avg_wavelength)

# Constants
laser_wavelength = 632.8e-9  # meters (for HeNe laser)

# Lists to store results
v_max_list = []
c_inc = []
c_dec = []

# Folder containing the data files
folder = "dag1"

# Loop through each file in the folder
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)			
    data = np.loadtxt(file_path, skiprows=3)

    freq, A, B = data.T

    # Find the midpoint where A is maximum
    mid = np.argmax(A)

    # Split the data into two halves
    A1, B1 = A[:mid], B[:mid]  # First half (increasing V)
    A2, B2 = A[mid:], B[mid:]  # Second half (decreasing V)

    # Plot the data
    plt.plot(A1, B1, label='First Half')
    plt.plot(A2, B2, label='Second Half')

    # Find peaks and lows for both halves
    p1, l1 = peaks(A1, B1)  # Peaks and lows for increasing V
    p2, l2 = peaks(A2, B2)  # Peaks and lows for decreasing V

    # Calculate the wavelength for both halves
    lambda_V1 = wave_len(p1, l1)  # ΔV for increasing
    lambda_V2 = wave_len(p2, l2)  # ΔV for decreasing

    print(f"ΔV (Increasing): {lambda_V1:.5f} V")
    print(f"ΔV (Decreasing): {lambda_V2:.5f} V")

    # Compute the piezoelectric constant C for both cases
    C1 = laser_wavelength / (2 * lambda_V1)
    C2 = laser_wavelength / (2 * lambda_V2)
    
    # Average the two values of C
    C_avg = (C1 + C2) / 2

    print(f"C (Increasing): {C1:.5e} m/V")
    print(f"C (Decreasing): {C2:.5e} m/V")
    print(f"C (Average): {C_avg:.5e} m/V")

    # Plot settings
    plt.xlabel('A (V)')
    plt.ylabel('B (V)')
    plt.title(r'Wave Analysis $V_{max}=$' + f"{A[mid]:.1f} V")
    plt.legend()
    plt.show()

    # Store results
    v_max_list.append(A[mid])  # Store V_max
    c_inc.append(C1)  # Store computed C for increasing V
    c_dec.append(C2)  # Store computed C for decreasing V

# Convert to NumPy arrays for easier analysis
v_max_list = np.array(v_max_list)
c1_val = np.array(c_inc)
c2_val = np.array(c_dec)

# Plot C vs. V_max
plt.figure(figsize=(8,6))
plt.scatter(v_max_list, c1_val, color='blue', label=r"$C_{increasing}$")
plt.scatter(v_max_list, c2_val, color='red', label=r"$C_{decreasing}$")
plt.xlabel(r"$V_{max}$ (V)")
plt.ylabel(r"Piezoelectric Constant $C$ (m/V)")
plt.title("Variation of Piezoelectric Constant with $V_{max}$")
plt.legend()
plt.grid(True)
plt.show()

# Print Summary Statistics
print("\nFinal Summary:")
print(f"Average C (Increasing): {np.mean(c1_val):.5e} m/V")
print(f"Standard Deviation of C (Increasing): {np.std(c1_val):.5e} m/V")
print(f"Min C (Increasing): {np.min(c1_val):.5e} m/V, Max C (Increasing): {np.max(c1_val):.5e} m/V")
print(f"Average C (Decreasing): {np.mean(c2_val):.5e} m/V")
print(f"Standard Deviation of C (Decreasing): {np.std(c2_val):.5e} m/V")
print(f"Min C (Decreasing): {np.min(c2_val):.5e} m/V, Max C (Decreasing): {np.max(c2_val):.5e} m/V")
