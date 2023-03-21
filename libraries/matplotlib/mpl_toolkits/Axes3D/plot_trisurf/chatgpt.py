#!/usr/bin/env python

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Generate some random data
x = np.random.rand(100)
y = np.random.rand(100)
z = np.sin(x * y)

# Create a 3D plot and add a trisurf
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none')

# Add labels and title
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('Trisurf Example')

# Show the plot
plt.show()

