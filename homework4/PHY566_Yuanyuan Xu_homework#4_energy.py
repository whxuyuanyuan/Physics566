# course: PHY566
# date: 02/20/2016
# author: Yuanyuan Xu
# NetID: yx82

"""
Calculate the potential, kinetic and total energies for a driving frequency
close to resonance and plot the figures.
"""

util = __import__('PHY566_Yuanyuan Xu_homework#4_utilities')
from pylab import *

g = 9.8         # acceleration of gravity
l = 9.8         # length of the string
gamma = 0.25    # damping coefficient
alpha_D = 0.2   # amplitude of driving force
omega_D = 0.93  # driving frequency near resonance
tmax = 60       # duration time
theta, omega, t = util.runge_kutta_linear(0.3, 0.4, omega_D, alpha_D, tmax)   # Runge-Kutta

potential = []  # potential energy
kinetic = []    # kinetic energy
total = []      # total energy

for i in range(len(theta)):
    potential.append(0.5 * g * l * theta[i] ** 2)  # V = 1/2*mgl(theta)^2
    kinetic.append(0.5 * (l * omega[i]) ** 2)      # T = 1/2*ml^2(omega)^2
    total.append(potential[-1] + kinetic[-1])      # E = T + V

# plot
plot(t, potential, label='potential energy')
plot(t, kinetic, label='kinetic energy')
plot(t, total, label='total energy')
grid()
legend()
xlabel('time (s)')
ylabel('energy')
fig = gcf()
fig.set_size_inches([10, 5])
savefig('energy.eps')