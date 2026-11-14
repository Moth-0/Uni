import numpy as np

class Potential1D:

    alpha = 10.0

    def __init__(self, k1x=5.0, k2x=2.0, deltaE=1, xmin=-5, xmax=5, x1=-1, x2=2):
        self.xmin = xmin
        self.xmax = xmax
        self.x1 = x1
        self.x2 = x2
        self.k1x = k1x
        self.k2x = k2x
        self.deltaE = deltaE
        print('deltaE',deltaE)

    def limits(self):
        return (self.xmin, self.xmax)

    def V1(self, x):
        return 0.5 * (self.k1x * (x - self.x1)**2)
    
    def V2(self, x):
        return 0.5 * (self.k2x * (x - self.x2)**2) + self.deltaE

    def dV1(self, x):
        return self.k1x * (x - self.x1)

    def dV2(self, x):
        return self.k2x * (x - self.x2)

    def __call__(self, x):
        return -1.0 / self.alpha * np.log(np.exp(-self.alpha * self.V1(x)) + np.exp(-self.alpha * self.V2(x)))

    def forces(self, x):
        V1 = self.V1(x)
        V2 = self.V2(x)
        dV1 = self.dV1(x)
        dV2 = self.dV2(x)

        w1 = np.exp(-self.alpha * V1)
        w2 = np.exp(-self.alpha * V2)

        numerator = w1 * dV1 + w2 * dV2
        denominator = w1 + w2

        return -numerator / denominator  # = -dV/dx

class Particle:

    def __init__(self, potential_1d, P0=0.):
        self.potential_1d = potential_1d
        self.pos = np.array([P0],dtype='float64')
        self.velocities = np.zeros(self.pos.shape)

    @property
    def forces(self):
        return self.potential_1d.forces(*self.pos)
    
    def set_positions(self,pos):
        self.pos = pos
        
    def get_positions(self):
        return self.pos.copy()

    @property
    def potential_energy(self):
        return self.potential_1d(*self.pos)

    @property
    def kinetic_energy(self):
        return 0.5 * np.sum(self.velocities**2)

    def set_velocities(self,velocities):
        self.velocities[:] = velocities

    def get_velocities(self):
        return self.velocities.copy()

class Simulation(Particle):
    
    def __init__(self, *args, kT=1.5, Nsample_size=1000, E0=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._sample = None
        self.Nsample_size = Nsample_size
        self._kT = kT
        self.E0 = E0

    @property
    def kT(self):
        return self._kT
    
    @kT.setter
    def kT(self,new_kT):
        print('... changing kT')
        if self._kT != new_kT:
            self._sample = None
            self._kT = new_kT

    @property
    def sample(self):
        if self._sample is None:
            self.setup_sample()
        return self._sample
    
    def estimate_from_sample(self, property):
        numerator = 0
        for s in self.sample:
            numerator += property(s)
        denominator = len(self.sample)
        return numerator / denominator

    def get_populations(self):
        pop_left = np.sum(np.where(self.sample < 0,1,0))
        pop_right = np.sum(np.where(self.sample >= 0, 1, 0))
        pops = np.array([pop_left,pop_right],dtype='float64')
        pops /= np.sum(pops)
        return pops.tolist()

    def title(self):
        ax.set_title(f'V(x), P(x)')

    def plot_potential(self, ax, color='C3'):
        xlimits = self.potential_1d.limits()
        xs = np.linspace(*xlimits, 100)
        ax.plot(xs, self.potential_1d(xs), color=color)
    
    
    def plot_probability(self, ax, xwidth=0.25, color='C3',start_index=0,end_index=None):
        #xlimits = self.potential_1d.limits()
        #xs = np.arange(*xlimits, xwidth)
        #ax.plot(xs, self.potential_1d(xs), color=color)
        self.plot_potential(ax, color=color)
        #ax.plot(xs, [self.potential_1d.forces(x) for x in xs], color=color)
        xs = np.linspace(min(self.sample),max(self.sample),30).ravel()
        print('A',xs)
        bars, xs_edges = np.histogram(self.sample,xs)
        xcenters = (xs_edges[:-1] + xs_edges[1:]) / 2
        delta_xvals = (xcenters[1] - xcenters[0])
        P = bars / np.sum(bars) / delta_xvals
        width = delta_xvals * 0.8
        if self.E0 is not None:
            bottom = self.E0
        else:
            bottom = self.kT
        if end_index is None:
            end_index = len(xcenters)
        ax.bar(xcenters[start_index:end_index], P[start_index:end_index]*20, width=width, bottom=bottom, facecolor=color, alpha=0.6)
        ax.set_title(self.title())
        ax.set_xlabel('x')
        #Pleft, Pright = self.get_populations()
        #ax.text(-4,12,'$P_{left}=$' + f'{Pleft:4.2f}', color=color, alpha=0.8)
        #ax.text(0,12,'$P_{right}=$' + f'{Pright:4.2f}', color=color, alpha=0.8)

    def plot_sample_trajectory(self, ax, max_points=None):
        pass

def velocity_verlet(cluster, N=100, dt=0.01):
    for _ in range(N):
        r = cluster.get_positions()
        v = cluster.get_velocities()
        a_t = cluster.forces
        r += v * dt + 0.5 * a_t * dt**2
        cluster.set_positions(r)
        a_t_dt = cluster.forces
        v += 0.5 * (a_t + a_t_dt) * dt
        cluster.set_velocities(v)

def andrea_anderson_thermostat(md):
    v = md.get_velocities()
    v = np.sqrt(md.kT) * np.random.randn(*v.shape)
    #v -= np.mean(v,axis=0)
    md.set_velocities(v)

class MolDyn(Simulation):

    def __init__(self, *args, Nvelocity_verlet=50, **kwargs):
        self.Nvelocity_verlet = Nvelocity_verlet
        super().__init__(*args, **kwargs)

    def plot_sample_trajectory(self, ax, max_points=None):
        if max_points is None:
            max_points = len(self.sample)
        x = self.sample[:max_points]
        ax.plot(x, np.linspace(0,1,len(x)), color='k')

class CanonicalMD(MolDyn):

    def title(self):
        ax.set_title(f'V(x), P(x), kT={self.kT}')
    
    def setup_sample(self):

        self._sample = []
        for _ in range(self.Nsample_size):
            andrea_anderson_thermostat(self)
            velocity_verlet(self,N=self.Nvelocity_verlet)

            self._sample.append(np.array(self.pos.copy()))
        self._sample = np.array(self._sample)
        
        print('Sample size:',self.sample.shape)

class MicroCanonicalMD(MolDyn):

    def title(self):
        return f'V(x), P(x), E={self.potential_energy + self.kinetic_energy}'
    
    def setup_sample(self):

        self._sample = []
        for _ in range(self.Nsample_size):
            velocity_verlet(self,N=self.Nvelocity_verlet)

            self._sample.append(np.array(self.pos.copy()))
        self._sample = np.array(self._sample)
        
        print('Sample size:',self.sample.shape)

