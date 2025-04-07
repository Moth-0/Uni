from scipy.optimize import curve_fit

class ez_curve_fit: 
    def __init__(self, func, x, y, y_err=None, p0=None): 
        self.x = x
        self.y = y
        if y_err:
            self.y_err = y_err
        self.func = func
        if p0:
            self.p0 = p0
        else: 
            self.p0 = 

    
    def fit(self): 
        popt, pcov = curve_fit(self.func, self.x, self.y, p0=self.p0, sigma=self.y_err, absolute_sigma=True)