# course: PHY566
# date: 02/20/2016
# author: Yuanyuan Xu
# NetID: yx82

"""
This code contains four useful functions:
    1. Euler-Cromer method (euler_cromer);
    2. Euler-Cromer method for motion equation with small angle approximation (euler_cromer_saa);
    3. Runge-Kutta method (runge_kutta);
    4. Runge-Kutta method for motion equation with small angle approximation (runge_kutta_saa).
"""

from math import *

g = 9.8         # acceleration of gravity
l = 9.8         # length of the string
gamma = 0.25    # damping coefficient
dt = 0.001      # time step


def f_nonlinear(th, om, t, omega_D, alpha_D):
    """
    1st order differential equation: d(omega)/dt = f(theta, omega, t).
    :param th: angle.
    :param om: angular velocity.
    :param t: time.
    :param omega_D: frequency of driving force.
    :param alpha_D: amplitude of driving force.
    :return: f(theta).
    """
    global g, l, gamma, dt
    return - (g / l) * sin(th) - 2 * gamma * om + alpha_D * sin(omega_D * t)


def f_linear(th, om, t, omega_D, alpha_D):
    """
    1st order differential equation using small angle approximation: d(omega)/dt = f(theta).
    :param th: angle.
    :param om: angular velocity.
    :param t: time.
    :param omega_D: frequency of driving force.
    :param alpha_D: amplitude of driving force.
    :return: f(theta).
    """
    global g, l, gamma, dt  # declare global variables
    return - (g / l) * th - 2 * gamma * om + alpha_D * sin(omega_D * t)


def euler_cromer_nonlinear(theta0, omega0, omega_D, alpha_D, tmax):
    """
    Use Euler-Cromer's method to solve the differential equation of oscillatory motion.
    :param theta0: initial angular velocity.
    :param omega0: initial angle.
    :param omega_D: frequency of driving force.
    :param alpha_D: amplitude of driving force.
    :param tmax: time duration.
    :return: n-arrays: angle, angular velocity, time.
    """
    global g, l, gamma, dt  # declare global variables
    omega = [omega0]        # angular velocity
    theta = [theta0]        # angle
    t = [0.0]               # time
    while t[-1] <= tmax:
        omega.append(omega[-1] + f_nonlinear(theta[-1], omega[-1], t[-1], omega_D, alpha_D) * dt)  # omega[i+1]
        theta_temp = theta[-1] + omega[-1] * dt  # temp value of theta[i+1]
        # check whether angle is out of range
        if theta_temp > pi:
            theta_temp -= 2 * pi
        if theta_temp < -pi:
            theta_temp += 2 * pi
        theta.append(theta_temp)  # theta[i+1]
        t.append(t[-1] + dt)  # t[i+1]
    return theta, omega, t


def euler_cromer_linear(theta0, omega0, omega_D, alpha_D, tmax):
    """
    Use Euler-Cromer method to solve the differential equation with small angle approximation of oscillatory motion.
    :param theta0: initial angular velocity.
    :param omega0: initial angle.
    :param omega_D: frequency of driving force.
    :param alpha_D: amplitude of driving force.
    :param tmax: time duration.
    :return: n-arrays: angle, angular velocity, time.
    """
    global g, l, gamma, dt  # declare global variables
    omega = [omega0]        # angular velocity
    theta = [theta0]        # angle
    t = [0.0]               # time
    while t[-1] <= tmax:
        omega.append(omega[-1] + f_linear(theta[-1], omega[-1], t[-1], omega_D, alpha_D) * dt)  # omega[i+1]
        temp = theta[-1] + omega[-1] * dt  # temp value of theta[i+1]
        # check whether angle is out of range
        if temp > pi:
            temp -= 2 * pi
        if temp < -pi:
            temp += 2 * pi
        theta.append(temp)  # theta[i+1]
        t.append(t[-1] + dt)  # t[i+1]
    return theta, omega, t


def runge_kutta_nonlinear(theta0, omega0, omega_D, alpha_D, tmax):
    """
    Use Runge-Kutta method to solve the differential equation of oscillatory motion.
    :param theta0: initial angular velocity.
    :param omega0: initial angle.
    :param omega_D: frequency of driving force.
    :param alpha_D: amplitude of driving force.
    :param tmax: time duration.
    :return: n-arrays: angular, angular velocity, time.
    """
    global g, l, gamma, dt  # declare global variables
    omega = [omega0]        # angular velocity
    theta = [theta0]        # angle
    t = [0.0]               # time
    while t[-1] <= tmax:
        th = theta[-1]      # theta[i]
        om = omega[-1]      # omega[i]
        # Runge-Kutta
        om1 = om; t1 = t[-1]
        om2 = om + 0.5 * f_nonlinear(th, om1, t1, omega_D, alpha_D) * dt; t2 = t[-1] + 0.5 * dt
        om3 = om + 0.5 * f_nonlinear(th, om2, t2, omega_D, alpha_D) * dt; t3 = t[-1] + 0.5 * dt
        om4 = om + f_nonlinear(th, om3, t3, omega_D, alpha_D) * dt; t4 = t[-1] + dt
        theta_temp = th + om * dt  # temp theta[i+1]
        # check whether angle is out of range
        if theta_temp > pi:
            theta_temp -= 2 * pi
        if theta_temp < -pi:
            theta_temp += 2 * pi
        theta.append(theta_temp)  # theta[i+1]
        omega.append(om + 1.0 / 6.0 * (f_nonlinear(th, om1, t1, omega_D, alpha_D) +
                                       f_nonlinear(th, om2, t2, omega_D, alpha_D) * 2 +
                                       f_nonlinear(th, om3, t3, omega_D, alpha_D) * 2 +
                                       f_nonlinear(th, om4, t4, omega_D, alpha_D)) * dt)  # omega[i+1]
        t.append(t[-1] + dt)  # t[i+1]
    return theta, omega, t


def runge_kutta_linear(theta0, omega0, omega_D, alpha_D, tmax):
    """
    Use Runge-Kutta method to solve the differential equation with small angle approximation of oscillatory motion.
    :param omega0: initial angle.
    :param theta0: initial angular velocity.
    :param omega_D: frequency of driving force.
    :param alpha_D: amplitude of driving force.
    :param tmax: time duration.
    :return: n-arrays: angle, angular velocity, time.
    """
    global g, l, gamma, dt  # declare global variables
    omega = [omega0]  # angular velocity
    theta = [theta0]  # angle
    t = [0.0]         # time
    while t[-1] <= tmax:
        th = theta[-1]          # theta[i]
        om = omega[-1]          # omega[i]
        # Runge-Kutta
        om1 = om; t1 = t[-1]
        om2 = om + 0.5 * f_linear(th, om1, t1, omega_D, alpha_D) * dt; t2 = t[-1] + 0.5 * dt
        om3 = om + 0.5 * f_linear(th, om2, t2, omega_D, alpha_D) * dt; t3 = t[-1] + 0.5 * dt
        om4 = om + f_linear(th, om3, t3, omega_D, alpha_D) * dt; t4 = t[-1] + dt
        theta_temp = th + om * dt  # temp theta[i+1]
        # check whether angle is out of range
        if theta_temp > pi:
            theta_temp -= 2 * pi
        if theta_temp < -pi:
            theta_temp += 2 * pi
        theta.append(theta_temp)  # theta[i+1]
        omega.append(om + 1.0 / 6.0 * (f_linear(th, om1, t1, omega_D, alpha_D) +
                                       f_linear(th, om2, t2, omega_D, alpha_D) * 2 +
                                       f_linear(th, om3, t3, omega_D, alpha_D) * 2 +
                                       f_linear(th, om4, t4, omega_D, alpha_D)) * dt)  # omega[i+1]
        t.append(t[-1] + dt)  # t[i+1]
    return theta, omega, t