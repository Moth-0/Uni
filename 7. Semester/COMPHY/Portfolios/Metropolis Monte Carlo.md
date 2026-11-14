---
marp: true
theme: gaia
math: true
---

# Metropolis Monte Carlo 

Simulating probability distribution of systems in thermal equilibrium. 

We only know the Boltzmann factor not the partition function. 

Propose new state x' from state x, symmetric proposal distribution. 

---

# Markov Chain 

![bg right:40% 80%](Pictures/Markov.png)

A Markov chain is a statistic sequence to determine state shifts based only on the current state. 


---

# Trial and Error 

Determine states based in acceptance criteria 


$$A(x|x') = \text{min}\left(1, \frac{P(x')}{P(x)}\right) 
= \text{min}\left(1, e^{-\Delta V / k_BT}\right)$$

So always down in energy and sometimes up. 

--- 

# Proposal Distribution

Needs to be symmetric: $\qquad T(x|x') = T(x'|x)$

$$E = [0, -\text{ln}(2), 0], \quad k_BT = 1/3$$

$$P = [0.1, 0.8, 0.1] \qquad\qquad\qquad \:$$

Using uniform and adjacent only proposal matrix gives ~ the same. But using non symmetric matrix gives wrong answer. 

(W02B) and (W02C) for plots with more states

---

# Continous Space 

Instead of $T$ being a matrix we now use probability distributions. 

Again we can use a uniform distribution, or an adjacent based proposal. 

(W02D) figures

--- 

# Initial Conditions Dependancy

The simulations can be very dependant of initial position $x_0$. 

(W02D) double well figure


---

# Optimization using Simulations

Instead of finding the fulle probability distribution, we can use the Metropolis Monte Carlo simulations to find the lowest energy in a system. 

Let Simulation run and record the state positions. 

(W03A) figure 

--- 

# Thermal Average

$$C_V$$