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
def sin_func(x, A, B, C, D):
        return A * np.sin(B * x + C) + D


folder = "dag1"

for file in os.listdir(folder):
    file_path = folder + "/" + str(file)			
    data = np.loadtxt(file_path, skiprows=3)

    freq, A, B = data.T

    mid = np.argmax(A)

    plt.plot(A[:mid],B[:mid])
    plt.plot(A[mid:], B[mid:])

    popt, pcov = curve_fit(sin_func, A[:mid],B[:mid])

    plt.plot(A[:mid], sin_func(A[:mid], *popt), label='Fitted Curve')
    plt.legend()
    plt.show()