# course: phys566
# date: 01/25/2016
# author: Yuanyuan Xu
# NetID: yx82

import pylab

# initialization
x = []
y1 = []
y2 = []

# read the file
fileInput = open('data.txt', 'r')

for line in fileInput:
    temp = line.split()
    x.append(float(temp[0]))
    y1.append(float(temp[1]))
    y2.append(float(temp[2]))

fileInput.close()

# visualization
pylab.plot(x, y1, color='r')
pylab.plot(x, y2, color='b')
pylab.grid()
pylab.title(r'$\sin(x)$ and $\frac{\sin(x)}{x}$')
pylab.xlabel(r'$x$')
pylab.ylabel(r'$y$')
pylab.legend([r'$\sin(x)$', r'$\frac{\sin(x)}{x}$'], 'upper left')

# save figure
pylab.savefig('figure.jpeg')
pylab.savefig('figure.eps')
pylab.savefig('figure.pdf')

pylab.show()



