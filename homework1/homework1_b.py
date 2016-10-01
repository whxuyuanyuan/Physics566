# course: phys566
# date: 01/25/2016
# author: Yuanyuan Xu
# NetID: yx82

import numpy as np

x = np.linspace(-10.0, 10.0, 401)  # 401 linear numbers from -10.0 to 10.0 in steps of 0.05

y1 = np.sin(x)
y2 = np.sin(x) / x

data = np.transpose(np.array([x, y1, y2]))
np.savetxt('data.txt', data, delimiter=' ', newline='\n')