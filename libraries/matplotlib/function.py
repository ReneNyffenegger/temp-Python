import numpy             as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.2)
y = [  0.4*x**3 + 0.8*x**2 - 3.1 * x - 21.4 for x in x ]

plt.plot(x, y)
plt.show()
