import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import inspect

class ez_curve_fit:
    '''
    Easier curve_fit all in one. 
    fit() to ececute and print the curve fit 
    plot(num_points=1000, label_data="Data", label_fit="Fit", show_errors=True) to plot the curve fittet function 
    '''
    def __init__(self, func, x, y, y_err=None, p0=None):
        # Validate func
        if not callable(func):
            raise TypeError("func must be a callable (i.e., a function).")

        # Validate x and y
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a NumPy array.")
        if not isinstance(y, np.ndarray):
            raise TypeError("y must be a NumPy array.")
        if x.shape != y.shape:
            raise ValueError("x and y must have the same shape.")

        # Validate y_err if provided
        if y_err is not None:
            if not isinstance(y_err, np.ndarray):
                raise TypeError("y_err must be a NumPy array.")
            if y_err.shape != y.shape:
                raise ValueError("y_err must have the same shape as y.")

        # Extract parameter names (excluding 'x')
        self.param_names = list(inspect.signature(func).parameters.keys())[1:]

        # Validate p0 if provided
        if p0 is not None:
            if not isinstance(p0, list):
                raise TypeError("p0 must be a list.")
            if len(p0) != len(self.param_names):
                raise ValueError(f"p0 must have {len(self.param_names)} elements to match the number of parameters in func.")

        # Store everything
        self.func = func
        self.x = x
        self.y = y
        self.y_err = y_err
        self.p0 = p0
        self.popt = None
        self.pcov = None
        self.perr = None

    def fit(self):
        self.popt, self.pcov = curve_fit(
            self.func,
            self.x,
            self.y,
            p0=self.p0,
            sigma=self.y_err,
            absolute_sigma= True if self.y_err is not None else False,
            maxfev= 10000
        )
        self.perr = np.sqrt(np.diag(self.pcov))
        self._print_params()

    def rescale_x(self, factor):
        """Rescale the x data (for plotting) by a given factor."""
        self.x_scaled = self.x * factor
        self._x_scale_factor = factor

    def rescale_y(self, factor):
        """Rescale the y data (for plotting) by a given factor."""
        self.y_scaled = self.y * factor
        self._y_scale_factor = factor

    def _print_params(self):
        print("Fitted parameters:")
        for i, (val, err) in enumerate(zip(self.popt, self.perr)):
            name = self.param_names[i] if i < len(self.param_names) else f"param_{i}"
            print(f"  {name}: {val:.5e} ± {err:.5e}")

    def plot(self, num_points=1000, x_label="x", y_label="y", title = "Curve Fit", show_errors=True, lineplot=False):
        # Use scaled x/y if available
        x_plot = getattr(self, "x_scaled", self.x)
        y_plot = getattr(self, "y_scaled", self.y)
        
        x_fit = np.linspace(min(self.x), max(self.x), num_points)
        y_fit = self.func(x_fit, *self.popt)

        # Rescale x_fit if x was scaled
        if hasattr(self, "_x_scale_factor"):
            x_fit = x_fit * self._x_scale_factor

        # Rescale y_fit if y was scaled
        if hasattr(self, "_y_scale_factor"):
            y_fit = y_fit * self._y_scale_factor

        plt.figure(figsize=(8, 5))
        # Plot Fit
        plt.plot(x_fit, y_fit, label="Fit", color='orange')

        # Check for styles and plot data
        if self.y_err is not None and show_errors:
            plt.errorbar(x_plot, y_plot, yerr=self.y_err, fmt='.', label="Data", capsize=3)
        elif lineplot:
            plt.plot(x_plot, y_plot, '-', label="Data")
        else: 
            plt.plot(x_plot, y_plot, 'o', label="Data")
        
        # Fit settings
        plt.legend()
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        
