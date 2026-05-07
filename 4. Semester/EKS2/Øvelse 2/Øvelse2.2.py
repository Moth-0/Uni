# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
import os

# Plot settings
plt.rc("axes", labelsize=18, titlesize=22)
plt.rc("xtick", labelsize=16, top=True, direction="in")
plt.rc("ytick", labelsize=16, right=True, direction="in")
plt.rc("legend", fontsize=16)

print("\n\n\n-------------------------------")

# Constants
LASER_WAVELENGTH = 632.8e-9  # meters (for HeNe laser)

# Sine function for fitting
def sine_func(x, A, λ, φ, D):
    return A * np.sin(2*np.pi / λ * x + φ) + D

def lin_func(x, k):
    return 1/2 * k * x

def Δs(max, v): 
    return np.abs(1/2 * LASER_WAVELENGTH / v * max)

def Δs_err(max, v, e):
    # Compute the propagated error using error propagation formula
    return np.abs(1/2 * max * LASER_WAVELENGTH / v**2) * e * 10**6


class WaveFunction:
    
    class Params: 
        def __init__(self, amplitude=None, wavelength=None, phase=None, offset=None):
            self.set(amplitude, wavelength, phase, offset)
        
        def set(self, amplitude, wavelength, phase, offset):
            assert(isinstance(amplitude, float))
            assert(isinstance(wavelength, float))
            assert(isinstance(phase, float))
            assert(isinstance(offset, float))

            self.amplitude = amplitude 
            self.wavelength = wavelength 
            self.phase = phase 
            self.offset = offset 

        def get(self):
            return [self.amplitude, self.wavelength, self.phase, self.offset]


    def __init__(self, A_input, B_input):
        assert(isinstance(A_input, np.ndarray)), f'{type(A_input)}'
        assert(isinstance(B_input, np.ndarray))

        self.A = A_input
        self.B = B_input

        self.params = self.Params(
            amplitude = (np.max(self.A) - np.max(self.B)) / 2,
            wavelength = self.find_wavelength(self.A, self.B),
            phase = 0.0,
            offset = np.mean(self.B)
        )

        self.err = None

    def fit(self, maxfev=1000): 
        try: 
            guess = self.params.get()
            popt, err = curve_fit(sine_func, self.A, self.B, p0=guess, maxfev=maxfev)
        except Exception as e:
            print(f'Got error: {e} skipping {r'$V_{max}=$' + f"{max(self.A):.1f} V"}')

        self.params.set(*popt)

        self.err = np.sqrt(np.diag(err))[1]

    
    def plot(self, name):
        print(f"ΔV ({name}): {self.get_length():.3g} V")
        print(f"Err ({name}): {self.err:.3g} V")
   

        # Calculate chi-squared for the fits
        y = sine_func(self.A, *self.params.get())
        chi2 = np.sum(((self.B - y) / self.err) ** 2)
        
        # Print chi-squared values
        print(f"Chi-squared ({name}): {chi2:.3g}")

        # Plot the data and the fits
        plt.plot(self.A, self.B*1000, label=name)
        plt.plot(self.A, y*1000, '--', label=f'Fit {name}')


    def find_wavelength(self, a, b):
        distance = int(50 * (90 / max(a)))
        peaks = find_peaks(b, height=0, distance=distance)[0]
        if len(peaks) > 1:
            avg_peak_distance = np.mean(np.diff(a[peaks]))
            return avg_peak_distance
        else:
            return a[-1] - a[0]
        
    def get_length(self):
        return self.params.get()[1]
    

# Lists to store results
v_inc_list = []
v_dec_list = []
v_inc_err = []
v_dec_err = []
v_max_list = []

# Folder containing the data files
folder = "dag3"

# Loop through each file in the folder
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    data = np.loadtxt(file_path, skiprows=3)

    freq, A, B = data.T

    A = A * 10 # From Amplicator 
    B = B * 0.001 # From mV to V


    # Find the midpoint where A is maximum
    mid = np.argmax(A)
    
    plt.plot(A, B)
    plt.legend(fontsize=12)
    plt.xlabel('A (V)')
    plt.ylabel('B (mV)')
    plt.title(r"Raw Data from Picoscope $V_{max}=$" + f"{A[mid]:.1f} V")
    plt.show()
    
    # Find the index where A goes over 0 and where it goes back under
    start = 30 + np.where(A[:mid] > 0)[0][0]
    end = mid + np.where(A[mid:] < 0)[0][0] - 20

    # Split the data into two halves
    A1, B1 = A[start:mid], B[start:mid]  # First half (increasing V)
    A2, B2 = A[mid:end], B[mid:end]  # Second half (decreasing V)

    inc = WaveFunction(A1, B1)
    dec = WaveFunction(A2, B2)

    inc.fit()
    dec.fit()

    print(f"{str(file)}")
    inc.plot('Increasing')
    dec.plot('Decreasing')
    
    plt.legend(fontsize=12)
    plt.xlabel('A (V)')
    plt.ylabel('B (mV)')
    plt.title(r"Wave Analysis $V_{max}=$" + f"{A[mid]:.1f} V")
    plt.show()

    # Store max
    v_max_list.append(A[mid])

    # Store results
    v_inc_list.append(inc.get_length())  # Store ΔV for increasing V
    v_dec_list.append(dec.get_length())  # Store ΔV for decreasing V

    # Store the errors
    v_inc_err.append(inc.err)
    v_dec_err.append(dec.err)



# Convert to NumPy arrays 
v_inc_list = np.array(v_inc_list)
v_dec_list = np.array(v_dec_list)
v_max_list = np.array(v_max_list)
v_inc_err = np.array(v_inc_err)
v_dec_err = np.array(v_dec_err)

v_lin = np.linspace(20, 95)

# Calculate Δs
Δs_inc = Δs(v_max_list, v_inc_list) * 10**6 # m to μm
Δs_dec = Δs(v_max_list, v_dec_list) * 10**6 

# Compute the propagated error using error propagation formula
Δs_inc_err = Δs_err(v_max_list, v_inc_list, v_inc_err)
Δs_dec_err = Δs_err(v_max_list, v_dec_list, v_dec_err)

# Linear fit for Δs vs. V_max
popt_inc, pcov_inc = curve_fit(lin_func, v_max_list, Δs_inc, sigma=Δs_inc_err, absolute_sigma=True)
popt_dec, pcov_dec = curve_fit(lin_func, v_max_list, Δs_dec, sigma=Δs_dec_err, absolute_sigma=True)
err_inc = np.sqrt(np.diag(pcov_inc))[0]
err_dec = np.sqrt(np.diag(pcov_dec))[0]

# Plot Δs vs. V_max with linear fit and error bars
plt.figure(figsize=(8,6))
plt.errorbar(v_max_list, Δs_inc, yerr=Δs_inc_err, fmt=".", label="Increasing", capsize=5)
plt.errorbar(v_max_list, Δs_dec, yerr=Δs_dec_err, fmt=".", label="Decreasing", capsize=5)
plt.plot(v_lin, lin_func(v_lin, *popt_inc), '--', label="Fit Increasing")
plt.plot(v_lin, lin_func(v_lin, *popt_dec), '--', label="Fit Decreasing")
plt.xlabel(r"$V_{max}$ (V)")
plt.ylabel(r"$\Delta s$ (μm)")
plt.title(r"Variation of $\Delta s$ with $V_{max}$")
plt.legend()
plt.show()

# Print Summary Statistics
print("\nFinal Summary:")
print(f"k increasing from fit: {popt_inc[0]:.3e} ± {err_inc:.3e} μm/V - value of Δs at 90V {popt_inc[0]/2*90:.3f} ± {err_inc/2*90:.3f} μm")
print(f"k decreasing from fit: {popt_dec[0]:.3e} ± {err_dec:.3e} μm/V - value of Δs at 90V {popt_dec[0]/2*90:.3f} ± {err_dec/2*90:.3f} μm")


# Calculate the percentage deviation at 150V from the error
k_avg = (popt_inc[0] + popt_dec[0]) / 2 
k_avg_err = (err_inc + err_dec) / 2
percentage_deviation = (k_avg_err) / k_avg * 100

print(f"Average k: {k_avg:.3e} ± {k_avg_err:.3e} μm/V and value at 90V {k_avg/2*90:.3f} μm ± {k_avg_err/2*90:.3f}%")