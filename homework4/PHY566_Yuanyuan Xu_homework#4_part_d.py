# course: PHY566
# date: 02/20/2016
# author: Yuanyuan Xu
# NetID: yx82

"""
Compare the result for two different nonlinear term: theta and sin(theta).
Change alpha_D to 1.2rad/s^2 and redo the calculation. (part d)
"""

util = __import__('PHY566_Yuanyuan Xu_homework#4_utilities')
from pylab import *

alpha_D = 0.2   # amplitude of driving force
omega_D = 0.93  # driving frequency near resonance
tmax = 60       # duration time

theta_saa, omega_saa, t_nl = util.runge_kutta_linear(0.3, 0.4, omega_D, alpha_D, tmax)   # linear
theta, omega, t = util.runge_kutta_nonlinear(0.3, 0.4, omega_D, alpha_D, tmax)           # nonlinear

# plot theta(t)
plot(t, theta, color='blue', label=r'$\sin{\theta}$')
plot(t_nl, theta_saa, linestyle=':', linewidth=1.5, color='red', label=r'$\theta$')
legend()
grid()
xlabel('time (s)')
ylabel(r'$\theta$')
fig = gcf()
fig.set_size_inches(10, 5)
savefig('part_d_comparison_theta.eps')
close()

# plot omega(t)
plot(t, omega, color='blue', label=r'$\sin{\theta}$')
plot(t_nl, omega_saa, linestyle=':', linewidth=1.5, color='red', label=r'$\theta$')
legend()
grid()
xlabel('time (s)')
ylabel(r'$\omega$')
fig = gcf()
fig.set_size_inches(10, 5)
savefig('part_d_comparison_omega.eps')
close()

alpha_D = 1.2  # increase alpha_D
theta, omega, t = util.runge_kutta_nonlinear(0.3, 0.4, omega_D, alpha_D, tmax)

# plot theta(t)
plot(t, theta)
xlabel('time (s)')
ylabel(r'$\theta$')
grid()
fig = gcf()
fig.set_size_inches(10, 5)
savefig('part_d_new_theta.eps')
close()

# plot omega(t)
plot(t, omega)
xlabel('time (s)')
ylabel(r'$\omega$')
grid()
fig = gcf()
fig.set_size_inches(10, 5)
savefig('part_d_new_omega.eps')
close()
