# course: PHY566
# date: 02/20/2016
# author: Yuanyuan Xu
# NetID: yx82

"""
Extract the full-width at half maximum (FWHM) of the resonance curve. (part b)
"""

import numpy as np
from pylab import *
from math import *

fileInput = open('data.txt', 'r')

th0 = []      # amplitude
phi = []      # phase shift
omega_D = []  # driving frequency

# load data
for line in fileInput:
    temp = line.split()
    omega_D.append(float(temp[0]))
    th0.append(float(temp[1]))
    phi.append(float(temp[2]))

max_val = max(th0)        # find maximum (resonance)
half_max = max_val / 2.0  # half maximum
half_om = []              # two points where th0(omega_D) = half_max
for i in range(len(th0) - 1):
    if min(th0[i], th0[i + 1]) <= half_max <= max(th0[i], th0[i + 1]):  # find possible range
        # estimate possible point
        half_om.append(omega_D[i] + (omega_D[i + 1] - omega_D[i]) / (th0[i + 1] - th0[i]) * (half_max - th0[i]))

full_width = half_om[1] - half_om[0]  # value of FWHM
gamma = 0.25      # damping ratio
print full_width  # print the value

# visualization
plot(omega_D, th0, marker='o', markersize=3)  # plot amplitude vs. frequency
grid()
xlabel(r'${\Omega}_D$')
ylabel(r'${\theta}_0$')
title('FWHM')
plot(half_om, [half_max, half_max], color='r', linewidth=1.2)  # plot FWHM
savefig('FWHM.eps')
