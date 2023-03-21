#!/usr/bin/env python

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define the Rosenbrock function
def rosenbrock(x, y, a=1, b=100):
    return (a - x)**2 + b*(y - x**2)**2

# Generate data for the plot
x = np.linspace(-0.5, 1.5, 25)
y = np.linspace(-1.0, 1.0, 25)

X, Y = np.meshgrid(x, y)

Z = rosenbrock(X, Y)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.view_init(elev=15, azim=35)

ax.plot_surface(X, Y, Z, cmap='viridis')

# Add labels and title
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('Rosenbrock Function')

# Show the plot
plt.show()
