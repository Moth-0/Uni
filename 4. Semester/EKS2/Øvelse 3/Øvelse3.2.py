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

def lin_func(x, a, b): 
    return a * x + b

print("\n\n\n-------------------------------")

path = "dag3"

degress = []

amplitudes = []
amax = []
amin = []

for folder in os.listdir(path):
    s = os.path.join(path, folder)
    deg = int(folder[9:])
    amps = []
    for file in os.listdir(s): 
        file_path = os.path.join(s, file)
        data = np.loadtxt(file_path, skiprows=3)

        _, A, _ = data.T # A in (V)

        amp = max(A) - min(A)
        amps.append(amp)
        
    degress.append(deg)
    amplitudes.append(np.average(amps))
    amax.append(max(amps))
    amin.append(min(amps))

degress = np.array(degress)
amplitudes = np.array(amplitudes)
amin = np.array(amin)
amax = np.array(amax)

yerr = [amplitudes - amin, amax - amplitudes]

# Sine function for fitting
def sine_func(x, A, λ, φ, D):
    return A * np.sin(λ * np.deg2rad(x) + φ)**2 + D

popt, pcov = curve_fit(
    sine_func, 
    degress, 
    amplitudes, 
    sigma=np.maximum(0.5 * (yerr[0] + yerr[1]), 1e-3), # Use yerr for weights
    absolute_sigma=True,
    p0=[1, np.pi/100, 0.2, 1.5], 
    maxfev=100000
)
print(popt)
plt.errorbar(degress, amplitudes, yerr=yerr, fmt=".", capsize=5, label="Data with error bars")

x_lin = np.linspace(0, 130, 1000)
plt.plot(x_lin, sine_func(x_lin, *popt), label="Fit")


plt.xlabel("Degrees")
plt.ylabel("Amplitude (V)")
plt.legend()
plt.show()
