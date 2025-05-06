# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
from scipy.stats import chi2
import os

# Plot settings
plt.rc("axes", labelsize=18, titlesize=22)
plt.rc("xtick", labelsize=16, top=True, direction="in")
plt.rc("ytick", labelsize=16, right=True, direction="in")
plt.rc("legend", fontsize=12)

def lin_func(x, a): 
    return a * x

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


    pres = float(file[0] + "." + file[1])
    pressure.append(pres)

    # Apply convolution to the data
    kernel = np.ones(100) / 100  # Simple moving average kernel
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
        plt.title(f"Data for {pres} bar")
        plt.xlabel("Time (s)")
        plt.ylabel("Detector (V)")
        plt.show()

print(peaks)

N = np.array(peaks)
Δp = np.array(pressure)

Δn = N * λ / l

# Unsertainties from measurements and find peaks 
p_uns = np.ones_like(Δp) * 0.05 
n_uns = np.ones_like(Δn) * 2 * λ / l # ± 2 peaks

# Fitting 
popt, pcov = curve_fit(
    lin_func, 
    Δp, Δn, 
    sigma=n_uns, 
    absolute_sigma=True)

a = popt[0]

a_err = np.sqrt(np.diag(pcov))[0]

# Print fit results
print(f"Δn/Δp = {a:.3e} ± {a_err:.3e}")

# Plot data and fit 
plt.errorbar(Δp, Δn, xerr=p_uns, yerr=n_uns, fmt='.', capsize=3, label="Data")
plt.plot(Δp, lin_func(Δp, *popt), label="Curve_fit")

# Teori
lin = np.linspace(min(Δp), max(Δp), 1000)
n_t = (1.000293 - 1)/1.01325
print(f"n_t = {n_t}")
plt.plot(lin, lin_func(lin, n_t), label="Theory")

#plt.title("Title")
plt.xlabel("Δp (bar)")
plt.ylabel("Δn")
plt.legend()
plt.show

n = 1 + a * 1.01325 # maybe 1.01325 to calculate in bar
print(f"Final result: \n n = {n} ± {a_err:.1e}")