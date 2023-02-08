import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 300)
y = np.sin(x)

plt.plot(x , y, "-g", label="sin(x)")

plt.show()
