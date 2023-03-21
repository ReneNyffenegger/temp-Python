#
#   https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid
#

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 101)
y = np.linspace(-2, 2, 101)

xx, yy = np.meshgrid(x, y)

zz = 2 * np.sin(xx) * np.cos(yy*1.4) + \
         np.sin(xx + yy)         + \
         np.cos(xx*1.3) * np.sin(yy)


h = plt.contourf(x, y, zz)

plt.axis('scaled')
plt.colorbar()
plt.show()
