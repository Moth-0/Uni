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

directory = "lamps"

# Iterate through all files in the directory
for folder in os.listdir(directory): 
    print(folder)
    folder_path = os.path.join(directory, folder)
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        
        # Load data from the file
        data = np.loadtxt(filepath, skiprows=14)
        
        # Extract x and y data
        x, y = data.T

        height = abs(max(y)-min(y)) * 0.3
        dist = 10
        prom = 500
        p = find_peaks(y, height, distance=dist, prominence=prom)[0]  

        print("Peaks")
        for peak in p: 
            print(x[peak])

        y_p, x_p = (list(t) for t in zip(*sorted(zip(y[p], x[p]))))

        plt.plot(x, y, "-", label="Data")
        plt.plot(x_p, y_p, "o", label="Peaks")
        plt.plot(x_p[-2:], y_p[-2:], ".")

        plt.title(folder)
        plt.xlabel(f"Wavelength (nm)")
        plt.ylabel("Intensity (counts)")
        plt.legend()
        plt.show()