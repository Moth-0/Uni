import numpy as np
import matplotlib.pyplot as plt

class DoubleWell():
    def __init__(self, k=1, x0=0, a1=-1, x1=1.5, λ=0.25):
        self.k = k
        self.x0 = x0
        self.a1 = a1
        self.x1 = x1
        self.λ = λ

    def V(self, x):
        return 0.5 * self.k * (x - self.x0)**2 + self.a1 * np.exp(-(x-self.x1)**2/(self.λ**2))

    def F(self, x):
        return -self.k * (x - self.x0) + (2 * (x - self.x1) / self.λ**2) * self.a1 * np.exp(-(x - self.x1)**2 / self.λ**2)


class OLFitPoly:
    def __init__(self, Ndegree):
        self.Ndegree = Ndegree
        self.beta = None

    def fit(self, X, y):
        X_aug = np.array([[x**p for p in range(self.Ndegree + 1)] for x in X])
        Xs = np.linalg.inv(X_aug.T @ X_aug) @ X_aug.T
        self.beta = Xs @ y
        return self.beta, X_aug

    def predict(self, X):
        if type(self.beta) == type(None):
            raise ValueError('No β, run .fit() first')
        
        X_aug = np.array([[x**p for p in range(self.Ndegree + 1)] for x in X])

        return X_aug @ self.beta

    def plot(self, ax, X): 
        y = self.predict(X)
        ax.scatter(X, y)

class PolyRidgeRegression:
    def __init__(self, Ndegree, lam, prior_model=None):
        self.Ndegree = Ndegree
        self.l = lam
        self.prior_model = prior_model
        self.beta = None

    def fit(self, X, y):
        X_aug = np.array([[x**p for p in range(self.Ndegree + 1)] for x in X])
        Il = self.l * np.identity(self.Ndegree + 1)
        Xs = np.linalg.inv((X_aug.T @ X_aug) + Il) @ X_aug.T
        
        # If a prior model is provided, fit to the residuals
        if self.prior_model is not None:
            # Assumes prior_model is a callable function or object with a predict method
            y_prior = self.prior_model.predict(X)
            y_target = y - y_prior
        else:
            y_target = y
            
        self.beta = Xs @ y_target
        return self.beta, X_aug

    def predict(self, X):
        if type(self.beta) == type(None):
            raise ValueError('No β, run .fit() first')
        
        X_aug = np.array([[x**p for p in range(self.Ndegree + 1)] for x in X])
        y_pred = X_aug @ self.beta
        
        # Add the prior prediction back when making a prediction
        if self.prior_model is not None:
            y_prior = self.prior_model.predict(X)
            y_pred = y_pred + y_prior
            
        return y_pred

    def plot(self, ax, X): 
        y = self.predict(X)
        ax.scatter(X, y)

class KernalRidgeRegression:
    def __init__(self, sigma, lam):
        self.sigma = sigma
        self.l = lam
        self.alpha = None

    def K(self, x1, x2):
        return np.exp(-(x1-x2)**2/(2*self.sigma**2))

    def fit(self, X, y):
        self.X_train = X
        self.N = len(X)

        self.K_fit = np.array([[self.K(X[i], X[j]) for j in range(self.N)] 
                                              for i in range(self.N)])

        self.alpha = np.linalg.inv(self.K_fit + self.l * np.identity(self.N)) @ y
        return self.alpha

    def predict(self, X):
        if type(self.alpha) == type(None):
            raise ValueError('No α, run .fit() first')

        M = len(X)

        K_pred = np.array([[self.K(X[i], self.X_train[j]) for j in range(self.N)]
                                                          for i in range(M)])
        
        return K_pred @ self.alpha

class PriorKernalRidgeRegression(KernalRidgeRegression):
    def __init__(self, *args, y0=0.0, **kwargs):
        super().__init__(*args, **kwargs)
        self.y0 = y0

    def fit(self, X, y):
        super().fit(X, y)
        
        self.alpha = (np.linalg.inv(self.K_fit + self.l * np.identity(self.N)) 
                      @ (y - self.y0))
        
        return self.alpha
    
    def predict(self, X):
        return super().predict(X) + self.y0


class PriorKernalRidgeRegression(KernalRidgeRegression):
    def __init__(self, *args, f0=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.f0 = f0

    def fit(self, X, y):
        super().fit(X, y)
        
        self.alpha = (np.linalg.inv(self.K_fit + self.l * np.identity(self.N)) 
                      @ (y - self.f0(X)))
        
        return self.alpha
    
    def predict(self, X):
        return super().predict(X) + self.f0(X)