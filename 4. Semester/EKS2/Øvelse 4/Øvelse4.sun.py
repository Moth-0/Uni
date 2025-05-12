# Imports
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.signal import find_peaks


# Plot settings
plt.rc("axes", labelsize=18, titlesize=22)
plt.rc("xtick", labelsize=16, top=True, direction="in")
plt.rc("ytick", labelsize=16, right=True, direction="in")
plt.rc("legend", fontsize=12)

print("\n\n\n-------------------------------")

# Directory containing the files
directory = "sun/sun"

# Normalized Planck's Law
def planck(x, T):
    h = 6.626e-34
    c = 3e8
    k = 1.381e-23
    out = (2*h*c**2) / (x**5 * (np.exp((h*c)/(x*k*T)) - 1))
    return out/np.max(out)

# Iterate through all files in the directory
for filename in os.listdir(directory):
    print(filename[:-4])
    filepath = os.path.join(directory, filename)
    
    # Load data from the file
    data = np.loadtxt(filepath, skiprows=3)
    
    # Extract x and y data
    x, y = data.T

    
    kernel = np.ones(8)   # Simple moving average kernel
    y = np.convolve(y, kernel, mode='same')

    # Normalize your y data
    y_scaled = y / np.max(y)


    plt.plot(x, y_scaled, "-", label="Data")
    x_lin = np.linspace(200, 1000, 1000)
    plt.plot(x_lin, planck(x_lin*1e-9, 5772), "g:", label="Sun spectrum")

    # Find max wavelength
    peak_index = np.argmax(y)
    lambda_peak_m = x[peak_index] * 1e-9  # in meters

    # Calculate temperature
    T_wien = 2.897e-3 / lambda_peak_m
    print(f"Estimated temperature via Wien's law: {T_wien:.1f} K, with peak {x[peak_index]}±{x[peak_index]-x[peak_index+10]}")

    # Find Dips
    height = 1
    dist = 1
    prom = 3000
    p = find_peaks(-y, distance=dist, prominence=prom)[0]  

    print(f"Peaks {x[p]}")
    plt.plot(x[p], y_scaled[p], ".", label="Dip")    

    plt.title(filename[:-4])
    plt.xlabel(f"Wavelength (nm)")
    plt.ylabel("Intensity (counts)")
    plt.legend()
    plt.show()