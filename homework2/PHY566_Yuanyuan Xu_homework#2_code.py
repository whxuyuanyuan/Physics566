# course: PHY566
# date: 02/01/2016
# author: Yuanyuan Xu
# NetID: yx82

import pylab
import numpy as np


def carbon_dating(activity_0, tau, dt, t_max):
    """
    Use Euler's method to integrate equation for radioactive decay.
    :param activity_0: activity of the isotope in the original sample.
    :param tau: decay constant.
    :param dt: time step interval.
    :param t_max: duration time.
    :return: 2 ndarrays. activity array and time array.
    """
    nsteps = int(t_max / dt + 1)  # total steps
    activity = [0.0] * nsteps  # initialize activity
    t = [0.0] * nsteps  # initialize timeline
    activity[0] = activity_0  # set initial value
    for i in range(nsteps - 1):
        t[i + 1] = t[i] + dt
        activity[i + 1] = activity[i] - activity[i] / tau * dt  # Euler's method
    return activity, t


def percent_error(analytical, numerical):
    """
    Calculate the percent error. Formula: |analytical solution - numerical solution| / analytical solution * 100 %
    :param analytical: analytical solution.
    :param numerical: numerical solution.
    :return: float number.
    """
    return np.abs(analytical - numerical) / analytical * 100

# numerical solution
tmax = 20000  # duration time
T_half = 5700  # half-life time
tau = T_half / np.log(2)  # decay constant
activity0 = 6.022 / 14 * 10 ** 14 / tau  # initial activity
activity_10, t_10 = carbon_dating(activity0, tau, 10, tmax)  # time-step width = 10 years
activity_100, t_100 = carbon_dating(activity0, tau, 100, tmax)  # time-step width = 100 years
activity_1000, t_1000 = carbon_dating(activity0, tau, 1000, tmax)  # time-step width = 1000 years

# analytical solution
t_analytical = np.linspace(0, tmax, tmax + 1)
activity_analytical = activity0 * np.exp(- t_analytical / tau)

# visualization
# plot the figure for analytical result and numerical results with step width = 10, 100.
pylab.plot(t_analytical, activity_analytical, color='black')  # analytical
pylab.plot(t_10, activity_10, color='red')  # step width = 10
pylab.plot(t_100, activity_100, color='blue')  # step width = 100
pylab.xlabel('time (years)')
pylab.ylabel('activity')
pylab.title('Activity of Radioactive Decay')
pylab.grid()
pylab.legend(['analytical result', 'time-step width = 10', 'time-step width = 100'], 'upper right')
pylab.savefig('figure_a.eps')
pylab.close()

# zoom (near time = 11400)
pylab.plot(t_analytical, activity_analytical, color='black')  # analytical
pylab.plot(t_10, activity_10, color='red', marker='v')  # step width = 10
pylab.plot(t_100, activity_100, color='blue', marker='*')  # step width = 100
pylab.xlabel('time (years)')
pylab.ylabel('activity')
pylab.title('Activity of Radioactive Decay')
pylab.xlim([11300, 11500])
pylab.ylim([1.27 * 10 ** 9, 1.33 * 10 ** 9])
pylab.grid()
pylab.legend(['analytical result', 'time-step width = 10', 'time-step width = 100'], 'upper right')
pylab.savefig('figure_a_zoomed.eps')
pylab.close()

# plot the figure for analytical result and numerical results with step width = 10, 100, 1000.
pylab.plot(t_analytical, activity_analytical, color='black')  # analytical
pylab.plot(t_1000, activity_1000, color='green', marker='x')  # time-step width = 1000
pylab.xlabel('time (years)')
pylab.ylabel('activity')
pylab.title('Activity of Radioactive Decay')
pylab.grid()
pylab.legend(['analytical result', 'time-step width = 1000'], 'upper right')
pylab.savefig('figure_b.eps')
pylab.close()

# zoom (near time = 12,000)
pylab.plot(t_analytical, activity_analytical, color='black')  # analytical
pylab.plot(t_1000, activity_1000, color='green', marker='x')  # time-step width = 1000
pylab.xlabel('time (years)')
pylab.ylabel('activity')
pylab.title('Activity of Radioactive Decay')
pylab.grid()
pylab.xlim([11900, 12100])
pylab.ylim([1.05 * 10 ** 9, 1.3 * 10 ** 9])
pylab.legend(['analytical result', 'time-step width = 1000'], 'upper right')
pylab.savefig('figure_b_zoomed.eps')
pylab.close()

# output results after 2 life-time (time = 12000)
print('After 2 life-time (12,000 years):')
print('Analytical solution: %f' % activity_analytical[12000])
print('Numerical solution and percent error:')
print('time-step width =   10 years: %20f       percent error: %f%%' % (activity_10[1200], percent_error(activity_analytical[12000], activity_10[1200])))
print('time-step width =  100 years: %20f       percent error: %f%%' % (activity_100[120], percent_error(activity_analytical[12000], activity_100[120])))
print('time-step width = 1000 years: %20f       percent error: %f%%' % (activity_1000[12], percent_error(activity_analytical[12000], activity_1000[12])))


