# course: PHY566
# date: 02/20/2016
# author: Yuanyuan Xu
# NetID: yx82

"""
Generate figures by using two different methods. (Part b)
"""

import numpy as np
from pylab import *
util = __import__('PHY566_Yuanyuan Xu_homework#4_utilities')

alpha_D = 0.2  # amplitude of driving force


def compare(omega_D, tmax, filename):
    """
    Compare the theta(t) and omega(t) for Euler-Cromor method and Runge-Kutta method.
    :param omega_D: driving frequency
    :param tmax: time duration.
    :param filename: filename of the figure.
    :return: null.
    """
    theta_ec, omega_ec, t_ec = util.euler_cromer_linear(0.6, 0.4, omega_D, alpha_D, tmax)  # Euler-Cromer
    theta_rk, omega_rk, t_rk = util.runge_kutta_linear(0.6, 0.4, omega_D, alpha_D, tmax)   # Runge-Kutta
    subplot(2, 1, 1)  # plot theta(t)
    plot(t_ec, theta_ec, color='r', linewidth=1, label='Euler-Cromer')
    plot(t_rk, theta_rk, color='b', linestyle=':', linewidth=1.5, label='Runge-Kutta')
    legend()
    grid()
    xlabel('time (s)')
    ylabel(r'$\theta$' + ' (radians)')
    subplot(2, 1, 2)  # plot omega(t)
    plot(t_ec, omega_ec, color='r', linewidth=1, label='Euler-Cromer')
    plot(t_rk, omega_rk, color='b', linestyle=':', linewidth=1.5, label='Runge-Kutta')
    legend()
    grid()
    xlabel('time (s)')
    ylabel(r'$\omega$' + ' (rad/s)')
    fig = gcf()
    fig.set_size_inches(16, 10, forward=True)  # set the size of the figure
    fig.savefig(filename + '.eps')
    close()

# case 1: omega_D = 0.5
compare(0.5, 100, 'comparison_1')

# case 2: omega_D = 1.0
compare(1.0, 100, 'comparison_2')

# case 3: omega_D = 1.5
compare(1.5, 100, 'comparison_3')
