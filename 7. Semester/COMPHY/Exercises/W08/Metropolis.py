import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


class Metropolis:
    def __init__(self, calc, initial_state, kT, step_size=0.1):
        """
        Base class for Metropolis Monte Carlo simulations.
        """
        # Ensure the state is a mutable float array
        self.state = np.array(initial_state, dtype=float)
        self.kT = kT
        self.step_size = step_size

        self.calc = calc
        
        # Data tracking arrays
        self.trajectory = [self.state.copy()]
        self.energies = [self.calc.V(self.state)] 
        
        self.accepted_moves = 0
        self.total_moves = 0

    def propose_move(self, state):
        """
        Proposes a new state. Default is a Gaussian random walk.
        Can be overridden if your system requires specific types of moves (like rotations).
        """
        return state + np.random.normal(scale=self.step_size, size=state.shape)

    def run(self, n_steps=10_000):
        """
        Runs the Metropolis Monte Carlo loop for n_steps.
        """
        for _ in range(n_steps):
            self.total_moves += 1
            current_energy = self.energies[-1]
            
            # Propose a move and calculate its energy
            proposed_state = self.propose_move(self.state)
            proposed_energy = self.calc.V(proposed_state)
            
            # Calculate energy difference
            de = proposed_energy - current_energy
            
            # Metropolis Acceptance Criterion
            if de < 0 or np.random.rand() < np.exp(-de / self.kT):
                self.state = proposed_state
                self.energies.append(proposed_energy)
                self.accepted_moves += 1
            else:
                self.energies.append(current_energy)
                
            # Record the state 
            self.trajectory.append(self.state.copy())
            
        return np.array(self.trajectory), np.array(self.energies)

    def thermal_avg_V(self):
        """Calculates the average potential energy from the simulation."""
        if not self.energies:
            raise Exception('Simulation not run')
        return np.mean(self.energies)

    def plot(self, ax, xmin=-5, xmax=5):
        """Plots the sampled distribution against the exact theoretical distribution."""
        
        if len(self.trajectory) <= 1: 
            raise Exception('Simulation not run')

        # Flatten the trajectory into a 1D array for the histogram
        positions = np.array(self.trajectory).flatten()

        bin_edges = np.linspace(xmin, xmax, 50)
        ax.hist(positions, bins=bin_edges, density=True, facecolor='C0', alpha=0.5, edgecolor='k', label='Simulated')

        x_grid = np.linspace(xmin, xmax, 200)
        
        # Safely evaluate the energy over the grid 
        v_exact = np.array([self.calc.V(np.array([x])) for x in x_grid])
        unnormalized_p = np.exp(-v_exact / self.kT)
        
        # Calculate Partition Function (Z) using scipy.integrate.quad
        Z, _ = quad(lambda x: np.exp(-self.calc.V(x) / self.kT), xmin, xmax)
        
        p_exact = unnormalized_p / Z
        
        ax.plot(x_grid, p_exact, 'k-', lw=2, label='p_exact')
        ax.plot(x_grid, v_exact, 'g-', lw=2, label='v_exact')

        ax.set_xlabel('x')
        ax.set_ylabel('Probability Density')
        ax.grid(True)
        
        # Using the rf-string for LaTeX formatting and variables
        ax.set_title(rf'$\langle V\rangle=${self.thermal_avg_V():.3f}, N = {self.total_moves}')
        ax.legend()

    @property
    def acceptance_ratio(self):
        if self.total_moves == 0:
            return 0.0
        return self.accepted_moves / self.total_moves