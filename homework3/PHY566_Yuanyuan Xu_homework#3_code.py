# course: PHY566
# date: 02/05/2016
# author: Yuanyuan Xu
# NetID: yx82

import numpy as np
from math import *
import pylab


def trajectory(theta, dt, **kwargs):
    """
    Use Euler's method to calculate the trajectory of the golf ball.
    :param theta: initial angle.
    :param dt: time step
    :param kwargs:
        type: 'ideal', 'drag', 'drag & spin'. (default = 'ideal')
        ball: 'smooth', 'dimpled'. (default = 'smooth')
    :return: 2 n-arrays of x and y coordinates.
    """
    m = 0.046                                           # mass of the ball
    A = 0.0014                                          # frontier area
    rho = 1.29                                          # density of air
    v0 = 70.0                                           # initial velocity
    C = 0                                               # default drag coefficient (ideal)
    S = 0                                               # default S_0 * omega / m (ideal)
    is_smooth = True                                    # true for smooth ball and false for dimpled ball
    g = 9.8                                             # acceleration of gravity
    type = kwargs.get('type', 'ideal')
    ball = kwargs.get('ball', 'smooth')
    # adjust parameters
    if ball == 'dimpled':
        is_smooth = False
    if type == 'drag':
        C = 0.5
        S = 0
    if type == 'drag & spin':
        C = 0.5
        S = 0.25
    x = [0.0]                                           # x-coordinate
    y = [0.0]                                           # y-coordinate
    vx = v0 * cos(theta)                                # x component of velocity
    vy = v0 * sin(theta)                                # y component of velocity
    while y[-1] > 0 or len(y) == 1:                     # y should be larger than 0 unless the initial value
        v = sqrt(vx ** 2 + vy ** 2)                     # absolute value of velocity
        if (not is_smooth) and (type != 'ideal'):       # for dimpled ball in unideal case
            if v > 14:
                C = 7.0 / v
        # Euler's method
        x.append(x[-1] + vx * dt)
        y.append(y[-1] + vy * dt)
        vx_temp = vx  # record the last vx (vx[i])
        vx = vx - C * rho * A * v * vx / m * dt - S * vy * dt  # vx[i+1]
        vy = vy - g * dt - C * rho * A * v * vy / m * dt + S * vx_temp * dt  # vy[i+1]
    return x, y


def plot_for_angles(theta, dt, type, ball, title, filename):
    """
    Plot the figure for different angles for a specific case.
    :param theta: narray containing the initial angles.
    :param dt: time-step.
    :param type: type of the case.
    :param ball: type of the ball.
    :param title: title of the figure.
    :param filename: filename of the generated figure.
    :return: Void.
    """
    style = ['dashdot', 'dotted', 'dashed', 'solid']  # control the line style
    for i in range(len(theta)):
        x, y = trajectory(theta[i] * pi / 180, dt, type=type, ball=ball)  # get the x- and y-coordinates of the ball.
        pylab.plot(x, y, label=r'$\theta = %2d^{\circ}$' % theta[i], linestyle=style[i], linewidth=1.2)  # plot
    pylab.legend(prop={'size':12})
    pylab.ylim(0)  # only show the result above the ground.
    pylab.xlabel('x (m)')
    pylab.ylabel('y (m)')
    pylab.title(title)
    pylab.savefig(filename + '.eps')  # save figure
    pylab.close()


def plot_for_cases(th, dt, mytype, myball):
    """
    Plot the figure for different cases with the same initial angle.
    :param th: initial angle.
    :param dt: time-step.
    :param mytype: narrays containing the types of the case.
    :param myball: narrays containing the types of the ball.
    :return:
    """
    style = ['dashdot', 'dotted', 'dashed', 'solid']  # control the line style
    for i in range(len(mytype)):
        x, y = trajectory(th * pi / 180, dt, type=mytype[i], ball=myball[i])  # get the x- and y-coordinates of the ball.
        pylab.plot(x, y, label=(myball[i] + '+' + mytype[i]), linestyle=style[i], linewidth=1.2)  # plot
    pylab.legend(loc='upper right', prop={'size':8})
    pylab.ylim(0)  # only show the result above the ground.
    pylab.xlabel('x (m)')
    pylab.ylabel('y (m)')
    pylab.title(r'$\theta = %2d^{\circ}$' % th)
    pylab.savefig('theta=%d.eps' % th)
    pylab.close()


# set parameters
theta = np.array([45, 30, 15, 9])                   # initial angles
dt = 0.001                                          # time step
mytitle = ['Ideal trajectory of a golf ball',
           'Trajectory of smooth golf ball with drag',
           'Trajectory of dimpled golf ball with drag',
           'Trajectory of dimpled golf ball with drag and spin']

myfilename = ['ideal', 'smooth_drag', 'dimpled_drag', 'dimpled_drag_spin']  # filenames for saving the figures
mytype = ['ideal', 'drag', 'drag', 'drag & spin']   # type of the case
myball = ['smooth', 'smooth', 'dimpled', 'dimpled']  # type of the ball

# plot the figures for different angles in the same case
for i in range(len(mytype)):
    plot_for_angles(theta, dt, mytype[i], myball[i], mytitle[i], myfilename[i])

# plot the figures for different cases with the same initial angle
for i in range(len(theta)):
    plot_for_cases(theta[i], dt, mytype, myball)
