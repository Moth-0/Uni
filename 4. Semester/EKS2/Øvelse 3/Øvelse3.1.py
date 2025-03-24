# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.stats import chi2
import os

# Plot settings
plt.rc("axes", labelsize=18, titlesize=22)
plt.rc("xtick", labelsize=16, top=True, direction="in")
plt.rc("ytick", labelsize=16, right=True, direction="in")
plt.rc("legend", fontsize=16)

print("\n\n\n-------------------------------")

plot = False

folder = "dag2"

l = 6.7 / 100 # Length tube (m)
λ = 632.8e-9  # meters (for HeNe laser)

pressure = []
peaks = []

for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    data = np.loadtxt(file_path, skiprows=3)

    t, A = data.T # t in (s) and A in (V)
    skip = 10000
    t = t[:-skip]
    A = A[:-skip]

    pres = float(file[0] + "." + file[1])
    pressure.append(pres)

    # Apply convolution to the data
    kernel = np.ones(10) / 10  # Simple moving average kernel
    A = np.convolve(A, kernel, mode='same')[1:]
    t = t[1:]

    height = 90
    
    # Distance
    dist = 500

    prom = 20  # Prominence: how much a peak stands out due to its height and location

    # Find peaks
    p = find_peaks(A, height=height, distance=dist, prominence=prom)[0]
    peaks.append(len(p))

    if plot: 
        # Plots
        plt.plot(t, A, "-", label="Data")
        plt.plot(t[p], A[p], ".", label="Peaks")
        plt.title(str(file))
        plt.xlabel("Time (s)")
        plt.ylabel("Detector (V)")
        plt.show()

print(pressure)
print(peaks)

N = np.array(peaks)
Δp = np.array(pressure)

Δn = N * λ / l

plt.plot(Δp, Δn, "o")
plt.xlabel("Δn")
plt.ylabel("Δn")
plt.show