# course: phys566
# date: 01/25/2016
# author: Yuanyuan Xu
# NetID: yx82

import numpy as np
import pylab

x = np.linspace(-10.0, 10.0, 401)  # 401 linear numbers from -10.0 to 10.0 in steps of 0.05

y1 = np.sin(x)
y2 = np.sin(x) / x

# visualization
pylab.plot(x, y1, color='r')
pylab.plot(x, y2, color='b')
pylab.grid()
pylab.title(r'$\sin(x)$ and $\frac{\sin(x)}{x}$')
pylab.xlabel(r'$x$')
pylab.ylabel(r'$y$')
pylab.legend([r'$\sin(x)$', r'$\frac{\sin(x)}{x}$'], 'upper left')
pylab.show()




