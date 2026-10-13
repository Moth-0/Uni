import numpy as np
import matplotlib.pyplot as plt 
from scipy.special import erf
from week07 import *

class MetropolisMonteCarlo:
    def __init__(self, factory, kT=0.15):
        self.factory = factory
        self.kT = kT

    def run(self, start_idx=0, steps=10_000):
        m = self.factory(start_idx)
        best_m = m
        destinct = {}

        for _ in range(steps):
            trial = self.factory(m.i)
            trial.shuffle_one_particle()

            de = trial.energy - m.energy

            if self.kT: cond = (de <= 0 or np.random.rand() <= np.exp(-de/self.kT))
            else: cond = (de <= 0)

            if cond:
                m = trial

            if m.energy < best_m.energy: 
                best_m = m

            desc_key = tuple(m.descriptor)
            if desc_key not in destinct:
                destinct[desc_key] = m

        self.best_m = best_m
        self.destinct = destinct

        return best_m, destinct

    def find_all_best(self):
        if not self.best_m:
            print('Simulation not run!')
            return
        
        # Find some states with the same descriptor to test uniqueness
        target_descriptor = self.best_m.descriptor
        matching_states = []

        # Search for matching states
        for i in range(self.factory.total): 
            if self.factory(i).descriptor == target_descriptor:
                matching_states.append(i)

        return matching_states

    def plot_best(self, num=4):
        if not self.best_m:
            print('Simulation not run!')
            return
        
        # Find some states with the same descriptor to test uniqueness
        target_descriptor = self.best_m.descriptor
        matching_states = []

        # Search for matching states
        i = 0
        while (len(matching_states) < num): 
            if self.factory(i).descriptor == target_descriptor:
                matching_states.append(i)
            i += 1

        fig, axes = plt.subplots(1, len(matching_states), figsize=(3 * len(matching_states), 3))
        for ax, idx in zip(axes, matching_states):
            self.factory(idx).plot(ax, label='Dual')
        plt.tight_layout()
        plt.show()
    
    def plot_distinct(self, num=4):
        if not self.destinct:
            print('Simulation not run!')
            return

        plots = min(num, len(self.destinct))
        fig, axes = plt.subplots(1, plots, figsize=(3*plots, 3))
        for ax, m in zip(np.atleast_1d(axes), list(self.destinct.values())[:plots]):
            m.plot(ax, label='Dual')
        plt.suptitle("Distinct structures by Energy")
        plt.tight_layout()
        plt.show()
        return axes


class TwoBinsDescriptor(DescriptorBase):

    centers = [1.0, 1.5]
    ylim = [0.0, 4.5]

    def __call__(self, pos):
        dist_vector = pdist(pos)
        hist = np.histogram(dist_vector, self.edges)
        return hist[0].tolist()

class ThreeBinsDescriptor(DescriptorBase):

    centers = [1.0, 1.5, 2.0]
    ylim = [0.0, 4.5]

    def __call__(self, pos):
        dist_vector = pdist(pos)
        hist = np.histogram(dist_vector, self.edges)
        return hist[0].tolist()

class ManyBinsDescriptor(DescriptorBase):
    centers = np.arange(1.0, 4.5, 0.5)
    ylim = [0, 25]
    
    def __call__(self, pos):
        dist_vector = pdist(pos)
        hist = np.histogram(dist_vector, bins=self.edges)[0]
        return hist.tolist()

class CoarseDescriptor(DescriptorBase):
    centers = np.arange(0.0, 6.6, 0.5)
    ylim = [0.0, 9.5]

    def __call__(self, pos):
        dist_vector = pdist(pos)
        hist = np.histogram(dist_vector, bins=self.edges)[0]
        return hist.tolist()

class FineDescriptor(DescriptorBase):
    centers = np.arange(0.0, 6.6, 0.1)
    ylim = [0.0, 9.5]

    def __call__(self, pos):
        dist_vector = pdist(pos)
        hist = np.histogram(dist_vector, bins=self.edges)[0]
        return hist.tolist()

class GaussianDescripter(DescriptorBase):
    def __init__(self, *args, sigma=0.5, dx=0.1, **kwargs):
        super().__init__(*args, **kwargs)
        self.sigma = sigma 
        self.dx = dx

    centers = np.arange(0.0, 6.6, 0.1)
    ylim = [0.0, 9.5]

    def gaussian(self, r, rj):
        return 1/np.sqrt(2*np.pi) / self.sigma*np.exp(-(r-rj)**2 / (2*self.sigma**2))

    def __call__(self, pos):
        dist_vector = pdist(pos)
        desc = []
        for xj in self.centers:
            gj = sum(self.gaussian(xj, dist_vector))*self.dx
            desc.append(gj)
        
        return desc

class ErfDescriptor(DescriptorBase):
    def __init__(self, *args, sigma=0.5, dx=0.1, **kwargs):
        super().__init__(*args, **kwargs)
        self.sigma = sigma 
        self.dx = dx

    centers = np.arange(0.0, 6.6, 0.1)
    ylim = [0.0, 9.5]

    def __call__(self, pos):
        dist_vector = pdist(pos)
        desc = []
        for xj in self.centers:
            gj = sum(0.5 * (erf((xj - dist_vector + self.dx/2) / np.sqrt(2)/self.sigma) 
                          - erf((xj - dist_vector - self.dx/2) / np.sqrt(2)/self.sigma)))
            desc.append(gj)
        
        return desc