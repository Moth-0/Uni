import numpy as np
import matplotlib.pyplot as plt

def thermostat(cluster, kT):
    '''
    Function for generating random velocities based on Tempereature
    Uses normal distribution
    Assumes mass = 1, ie. all atoms same size

    Arguments: 
        cluster: cluster class object with method '.get_velocity()' and '.set_velocity()'
        kT: float of k_bT as a temperature 

    Returns None, but changes the velocities of the non static atoms in the cluster object
    '''
    scale = np.sqrt(kT) # Assume m=1
    v_old = cluster.get_velocity()
    v_new = np.random.normal(0, scale, size=v_old.shape)
    
    # Zero out the velocity for all static atoms
    is_static = np.array(cluster.static)
    v_new[is_static] = 0.0 
    
    cluster.set_velocity(v_new)

def velocity_verlet(cluster, N=100, dt=0.01):
    '''
    Function for running method for updating positions and velocities of atom clusters. 

    Arguments: 
        cluster: cluster class object with velocity methods. 
        N: int for number of moves 
        dt: float for stepsize 

    Returns: Position, Energy
        Position: the updated position after all steps are completed
        Energy: The total energy of the full state after the full simulation 

    Changes the cluster objects positions and velocities. 
    '''
    a_t = cluster.forces # assume m=1
    r = cluster.get_positions()
    v = cluster.get_velocity()
    
    # Pre-calculate the mask for speed
    is_static = np.array(cluster.static)

    for _ in range(N):
        # 2. Prevent static atoms from accelerating
        a_t[is_static] = 0.0 
        v[is_static] = 0.0
        
        r += v*dt + 0.5*a_t*dt**2
        cluster.set_positions(r)

        a_dt = cluster.forces # assume m=1
        
        # 3. Prevent new forces from affecting static atoms
        a_dt[is_static] = 0.0 

        v += 0.5* (a_t + a_dt) * dt

        a_t = a_dt.copy()

    cluster.set_velocity(v)

    e = cluster.potential_energy + cluster.K
    return cluster.get_positions(), e
