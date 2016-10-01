# course: PHY566
# date: 02/20/2016
# author: Yuanyuan Xu
# NetID: yx82

"""
Compute |d(theta)| for several trajectories and estimate the Lyapunov exponent lambda of the system. (part e)
"""

util = __import__('PHY566_Yuanyuan Xu_homework#4_utilities')
from pylab import *
from math import *
import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b):
    """
    Model function f(x) = a * x + b.
    :param a: Lyapunov exponent.
    :param b: initial deviation.
    """
    return a * x + b

def lyapunov(alpha_D, theta0, omega0, number, tmax):
    """
    Plot the trajectories of two identical pendulums with slightly different initial
    value and plot |d_theta|. Then use model function to fit the curve and print the
    Lyapunov exponent for each trajectory.
    :param alpha_D: amplitude of driving force.
    :param theta0: initial angle.
    :param omega0: initial angular velocity.
    :param number: number of figures.
    :param tmax: duration time.
    :return: null.
    """
    omega_D = 0.666  # driving frequency near resonance
    d_theta0 = np.linspace(0.0009, 0.0011, number)  # generate different initial value around 0.001

    for i in range(number):
        theta1, omega1, t = util.runge_kutta_nonlinear(theta0 + d_theta0[i], omega0, omega_D, alpha_D, tmax)  # pendulum 1
        theta2, omega2, t = util.runge_kutta_nonlinear(theta0, omega0, omega_D, alpha_D, tmax)  # pendulum 2
        subplot(2, 1, 1)  # plot theta(t)
        plot(t, theta1, color='b', label='pendulum 1')
        plot(t, theta2, color='r', linestyle=':', label='pendulum 2')
        title(r'$\Delta\theta _{\mathrm{in}} = $ %.5f' % d_theta0[i])
        legend(prop={'size':6.5})
        grid()
        ylabel(r'$\theta$' + ' (radians)')
        subplot(2, 1, 2)  # plot omega(t)
        plot(t, omega1, color='b', label='pendulum 1')
        plot(t, omega2, color='r', linestyle=':', label='pendulum 2')
        legend(prop={'size':6.5})
        grid()
        xlabel('time (s)')
        ylabel(r'$\omega$' + ' (rad/s)')
        fig = gcf()
        fig.set_size_inches(9, 5, forward=True)  # set the size of the figure
        fig.savefig('trajectory_%.1f_%d.eps' %(alpha_D, i + 1))
        close()

        d_theta = []  # difference between theta1 and theta2
        for j in range(len(theta1)):
            d_theta.append(abs(theta1[j] - theta2[j]))
        guess = np.array([1.0, 0.001])  # initial guess for curve fitting
        # make numpy arrays
        t = np.array(t)
        d_theta = np.array(d_theta)
        p = np.log(d_theta)
        popt, pcov = curve_fit(func, t, p, guess)  # curve fitting
        y = np.exp(popt[0] * t + popt[1])
        print(popt[0])
        semilogy(t, d_theta, color='blue')
        semilogy(t, y, linestyle='--', color='red')
        grid()
        title(r'$\Delta\theta _{\mathrm{in}} = $ %.5f, $\lambda = $ %.5f' % (d_theta0[i], popt[0]))
        xlabel('time (s)')
        ylabel(r'$\Delta\theta$ (radians)')
        fig = gcf()
        fig.set_size_inches(9, 5, forward=True)  # set the size of the figure
        savefig('lyapunov_%.1f_%d.eps' %(alpha_D, i + 1))
        close()

lyapunov(0.2, 0.2, 0.2, 3, 60)      # alpha_D = 0.2, 3 sets of data
lyapunov(0.5, 0.2, 0.2, 3, 60)      # alpha_D = 0.5, 3 sets of data
lyapunov(1.2, 0.2, 0.2, 11, 100)    # alpha_D = 1.2, 11 sets of data
