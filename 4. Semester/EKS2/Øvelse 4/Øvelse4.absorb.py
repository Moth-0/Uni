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

directory = "salts"

for folder in os.listdir(directory):
    print(folder)
    path = os.path.join(directory, folder)
    a = 0.2
    sum_list = []
    for file in os.listdir(path):
        filepath = os.path.join(path, file)

        # Load data from the file
        data = np.loadtxt(filepath, skiprows=14)
        
        # Extract x and y data
        x, y = data.T
        
        # Remove points where y <= 0
        mask = y > 0
        x, y = x[mask], y[mask]

        sum_list.append(sum(y))

        plt.plot(x, y, "-", label=file[:2], color=str(folder), alpha=a)
        a += 0.2

    # Find relative concentration 
    for i, file in zip(sum_list, os.listdir(path)): 
        print(f"{file[:2]}: {i/sum_list[0]}")

    plt.title(folder)
    plt.xlabel(f"Wavelength (nm)")
    plt.ylabel("Absorbance (OD)")
    plt.legend()
    plt.show()