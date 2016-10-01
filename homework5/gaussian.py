import numpy as np
from math import *
import matplotlib.pyplot as plt
import random

x = np.linspace(-5, 5, 10000)
y = 1.0 / (sqrt(2.0 * pi)) * np.exp(- x ** 2 / 2.0)
plt.plot(x, y)

numbers = []
random.seed(1234)
count = 0
while count < 1000000:
    x1 = 2.0 * random.random() - 1.0
    x2 = 2.0 * random.random() - 1.0
    w = x1 ** 2 + x2 ** 2
    if w < 1.0:
        w = sqrt((-2.0 * log(w)) / w)
        y1 = x1 * w
        y2 = x2 * w
        numbers.append(y1)
        numbers.append(y2)
        count += 2

n, bins, patches = plt.hist(numbers, 1000, normed=1, facecolor='g', alpha=0.3)
plt.show()

