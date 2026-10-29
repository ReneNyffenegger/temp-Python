#!/usr/bin/env python3
#
#   https://www.johal.in/matplotlib-animations-dynamic-visualizations-in-python-for-real-time-data-display

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

# Initialize figure and axis

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 1)

# Initial line data
line, = ax.plot([], [], lw=2)

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Animation function: updates line with new data point
def animate(i):
    x = np.linspace(0, 10, 100)
    y = np.cumsum(np.random.random(100)) / 100   # Simulated real-time cumulative data
    line.set_data(x[:i%100+1], y[:i%100+1])
    return line,

# Create animation: 200 frames, 50ms interval for ~20 FPS
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)

# To display:
#   plt.show()
#
# For saving:
ani.save('real_time_line.gif', writer='pillow')

print("Animation object created successfully!")
