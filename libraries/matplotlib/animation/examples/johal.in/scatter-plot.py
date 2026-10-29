#!/usr/bin/env python3
#
# Real-Time Scatter Plot Animation for IoT Sensor Data
#

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.collections import PathCollection
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
scatter = ax.scatter([], [], c='red', s=50)

def init():
    scatter.set_offsets(np.empty((0, 2)))
    return scatter,

def animate(i):
    # Simulate streaming sensor data: position updates
    positions = np.random.randn(50, 2) * i / 10   # Evolving positions
    colors = np.random.rand(50)                   # Temperature-like values
    scatter.set_offsets(positions)
    scatter.set_array(colors)
    ax.set_title(f'Frame {i}: Real-Time Sensor Positions')
    return scatter,

# Animate at 30 FPS for smooth real-time feel
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=33, blit=False)

print("Scatter animation initialized for IoT visualization!")

plt.show()
