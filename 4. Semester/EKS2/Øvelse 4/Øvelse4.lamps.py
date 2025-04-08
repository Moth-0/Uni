# Imports
import numpy as np
import matplotlib.pyplot as plt
import os



# Plot settings
plt.rc("axes", labelsize=18, titlesize=22)
plt.rc("xtick", labelsize=16, top=True, direction="in")
plt.rc("ytick", labelsize=16, right=True, direction="in")
plt.rc("legend", fontsize=12)

print("\n\n\n-------------------------------")

directory = "lamps"

# Iterate through all files in the directory
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    
    # Load data from the file
    data = np.loadtxt(filepath, skiprows=14)
    
    # Extract x and y data
    x, y = data.T

    plt.plot(x, y, "-", label="Data")

    plt.title(filename)
    plt.legend()
    plt.show()