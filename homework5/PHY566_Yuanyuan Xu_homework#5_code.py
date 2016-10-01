import numpy as np
from math import *
import matplotlib.pyplot as plt
import random


def random_numbers(k, seed):
    """
    Generate k random numbers
    :param k: number of random numbers.
    :param seed: random seed.
    :return: null.
    """
    subdivisions = [10, 20, 50, 100]  # number of subdivisions
    numbers = []  # initialize
    random.seed(seed)  # set random seed
    for i in range(0, k):
        numbers.append(random.random())
    for i in range(len(subdivisions)):
        # plot histogram
        n, bins, patches = plt.hist(numbers, subdivisions[i], facecolor='g', alpha=0.3, normed=True)
        plt.xlabel('x')
        plt.ylabel('P(x)')
        plt.savefig('a_%d_%d.eps' % (k, subdivisions[i]))  # save figure
        plt.close()


def random_Marsaglia(k, seed):
    """
    Generate k Gaussian distributed random numbers.
    :param k: number of random numbers.
    :param seed: random seed.
    :return: null.
    """
    subdivisions = [10, 20, 50, 100]  # number of subdivisions
    numbers = []    # initialize
    random.seed(seed)   # set random seed
    count = 0  # counter
    # Marsaglia algorithm
    while count < k:
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
    for i in range(len(subdivisions)):
        # plot Gaussian function
        x = np.linspace(-5, 5, 10000)
        y = 1.0 / (sqrt(2.0 * pi)) * np.exp(- x ** 2 / 2.0)
        plt.plot(x, y, color='r')
        # plot histogram
        n, bins, patches = plt.hist(numbers, subdivisions[i], facecolor='b', alpha=0.3, normed=True)
        plt.xlabel('x')
        plt.ylabel('P(x)')
        plt.savefig('b_%d_%d.eps' % (k, subdivisions[i]))
        plt.close()

seed = 1234  # random seed
# part a
random_numbers(1000, seed)
random_numbers(1000000, seed)

# part b
random_Marsaglia(1000, seed)
random_Marsaglia(1000000, seed)