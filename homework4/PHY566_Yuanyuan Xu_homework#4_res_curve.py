# course: PHY566
# date: 02/20/2016
# author: Yuanyuan Xu
# NetID: yx82

"""
Plot the resonance curve and generate the data. (part b)
"""

import numpy as np
from scipy.optimize import curve_fit
from math import *
from pylab import *
util = __import__('PHY566_Yuanyuan Xu_homework#4_utilities')

def func(x, a, b, c):
    """
    Model function f(x) = th0 * sin(om * x + phi).
    :param a: amplitude.
    :param b: angular frequency.
    :param c: phase shift.
    """
    return abs(a) * sin(b * x + c)


def phase_shift(angle):
    """
    Set angle in the range of -pi to pi.
    :param angle: original phase shift.
    :return: phase shift within [-pi, pi].
    """
    if -pi <= angle <= pi:
        return angle
    if angle > pi:
        return phase_shift(angle - 2 * pi)  # recursion
    if angle < -pi:
        return phase_shift(angle + 2 * pi)  # recursion

alpha_D = 0.2  # amplitude of driving force
th0 = []  # amplitude
phi = []  # phase shift

omega_D = np.linspace(0.1, 1.5, 50)  # 50 different driving frequencies
for i in range(len(omega_D)):
    tmax = 50 + 30 / omega_D[i]  # make duration time reasonable (not too big or too small)
    theta, omega, t = util.runge_kutta_linear(0.2, 0.2, omega_D[i], alpha_D, tmax)
    # make numpy array
    theta = np.array(theta)
    t = np.array(t)
    guess = np.array([alpha_D, omega_D[i], 1.0])  # initial guess
    popt, pcov = curve_fit(func, t[len(t)/5 * 4: len(t)], theta[len(t)/5 * 4: len(t)], guess)  # curve fitting
    while np.sum(np.sqrt(np.diag(pcov))) > 10 ** -2:  # if the standard deviation error is big.
        guess += 0.05  # tune the initial guess
        popt, pcov = curve_fit(func, t[len(t)/8 * 7: len(t)], theta[len(t)/8 * 7: len(t)], guess)  # curve fitting
    th0.append(abs(popt[0]))  # positive amplitude
    phi.append(phase_shift(popt[2]))  # phase shift

# plot the figure
subplot(2, 1, 1)
plot(omega_D, th0, marker='o', markersize=3)  # plot amplitude vs. frequency
grid()
xlabel(r'${\Omega}_D$')
ylabel(r'${\theta}_0$')
title('amplitude vs. driving frequency')
subplot(2, 1, 2)
plot(omega_D, phi, marker='o', markersize=3)  # plot phase shift vs. frequency
grid()
xlabel(r'${\Omega}_D$')
ylabel(r'${\phi}$')
yticks([-pi, -pi / 2, 0], [r'$-\pi$', r'$-\pi / 2$', r'$0$'])
title('phase shift vs. driving frequency')
tight_layout()
savefig('resonance_curve.eps')

# save data
savetxt('data.txt', np.transpose(np.array([omega_D, th0, phi])), delimiter=' ', newline='\n')




