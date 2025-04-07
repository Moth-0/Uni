# Imports
import numpy as np
import matplotlib.pyplot as plt
import os
from Lib.mypylib import ez_curve_fit

# Plot settings
plt.rc("axes", labelsize=18, titlesize=22)
plt.rc("xtick", labelsize=16, top=True, direction="in")
plt.rc("ytick", labelsize=16, right=True, direction="in")
plt.rc("legend", fontsize=12)

print("\n\n\n-------------------------------")

# Directory containing the files
directory = "sun"

# Planck's Law
def planck(x, T, scale):
    h = 6.626e-34
    c = 3e8
    k = 1.381e-23
    return scale * (2*h*c**2) / (x**5 * (np.exp((h*c)/(x*k*T)) - 1))

# Iterate through all files in the directory
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    
    # Load data from the file
    data = np.loadtxt(filepath, skiprows=3)
    
    # Extract x and y data
    x, y = data.T

    x = x * 1e-9  # convert from nm to meters

    y_scaled = y / np.max(y)
    print(np.max(y))
    
    fit = ez_curve_fit(planck, x, y_scaled, p0=[5800, 1e-8])
    fit.fit()
    # Rescale for plotting
    fit.rescale_x(1e9)   # Convert x from meters to nanometers
    fit.plot(title=filename, lineplot=True)
    x_lin = np.linspace(200, 1000, 1000)
    plt.plot(x_lin, planck(x_lin*1e-9, 5772, 1)*1e-9)
    plt.show()
