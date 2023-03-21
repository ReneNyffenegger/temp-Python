#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the vertices of the dodecahedron
phi = (1 + np.sqrt(5))/2
vertices = np.array([
    [-1, -1, -1],
    [-1, -1, 1],
    [-1, 1, -1],
    [-1, 1, 1],
    [1, -1, -1],
    [1, -1, 1],
    [1, 1, -1],
    [1, 1, 1],
    [0, -1/phi, -phi],
    [0, -1/phi, phi],
    [0, 1/phi, -phi],
    [0, 1/phi, phi],
    [-1/phi, -phi, 0],
    [-1/phi, phi, 0],
    [1/phi, -phi, 0],
    [1/phi, phi, 0],
    [-phi, 0, -1/phi],
    [-phi, 0, 1/phi],
    [phi, 0, -1/phi],
    [phi, 0, 1/phi]
])

# Define the faces of the dodecahedron
faces = np.array([
    [0, 8, 9, 4, 16],
    [0, 12, 13, 1, 8],
    [0, 16, 17, 2, 12],
    [1, 13, 14, 5, 18],
    [1, 8, 9, 3, 13],
    [2, 9, 10, 6, 17],
    [2, 12, 14, 7, 10],
    [3, 9, 10, 6, 15],
    [3, 13, 14, 7, 19],
    [4, 9, 10, 6, 16],
    [4, 16, 17, 2, 11],
    [5, 13, 14, 7, 18],
    [5, 18, 19, 3, 13],
    [6, 10, 11, 5, 17],
    [6, 15, 19, 3, 10],
    [7, 14, 15, 6, 19],
    [7, 18, 19, 3, 14],
    [0, 8, 11, 5, 12],
    [1, 8, 11, 5, 13],
    [2, 12, 11, 5, 14],
    [4, 16, 11, 5, 13],
    [4, 9, 11, 5, 16],
    [7, 14, 11, 5, 18],
    [7, 19, 11, 5, 14]
])


# Create a new 3D plot and set the projection to '3d'
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vertices and the faces
ax.plot_trisurf(vertices[:,0], vertices[:,1], faces, vertices[:,2], cmap=plt.cm.Spectral)

# Set the limits and labels for the axes
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
