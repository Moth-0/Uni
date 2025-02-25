# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
import os as os 

# Plot settings
plt.rc("axes", labelsize=18, titlesize=22)   # skriftstørrelse af `xlabel`, `ylabel` og `title`
plt.rc("xtick", labelsize=16, top=True, direction="in")  # skriftstørrelse af ticks, vis også ticks øverst og vend ticks indad
plt.rc("ytick", labelsize=16, right=True, direction="in") # samme som ovenstående
plt.rc("legend", fontsize=16) # skriftstørrelse af figurers legends

# Functions
def sin_func(x, A, θ, φ, C):
        return A * np.sin(θ * x + φ) + C

def peaks(a,b): 
    peak = find_peaks(b, -0.5, 0, 100000)[0]
    low = find_peaks(-b, 1.7, 0, 100000)[0]
    
    plt.plot(a[peak], b[peak], "o")
    plt.plot(a[low], b[low], "o")

folder = "dag1"

for file in os.listdir(folder):
    file_path = folder + "/" + str(file)			
    data = np.loadtxt(file_path, skiprows=3)

    freq, A, B = data.T

    mid = np.argmax(A)

    A1, B1 = A[:mid], B[:mid]
    A2, B2 = A[mid:], B[mid:]

    plt.plot(A1, B1, label='First Half')
    plt.plot(A2, B2, label='Second Half')

    peaks(A1,B1)
    peaks(A2,B2)

    """
    # Initial guesses for the fit parameters
    initial_guess = [5, 3, 0, 0]
    
    # Fit for the first half
    popt1, pcov1 = curve_fit(sin_func, A[:mid], B[:mid], p0=initial_guess, maxfev=10000)
    plt.plot(A[:mid], sin_func(A[:mid], *popt1), label='Fit First Half')

    # Fit for the second half
    popt2, pcov2 = curve_fit(sin_func, A[mid:], B[mid:], p0=initial_guess, maxfev=10000)
    plt.plot(A[mid:], sin_func(A[mid:], *popt2), label='Fit Second Half')
    """
    #plt.legend()
    plt.show()