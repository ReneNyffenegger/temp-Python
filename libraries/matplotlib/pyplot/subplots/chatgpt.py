import numpy as np
import matplotlib.pyplot as plt

# Data for the plots
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.log(x)
y4 = np.exp(-x)

# Create the figure and subplots
fig, axs = plt.subplots(2, 2)

# First subplot
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('sin(x)')

# Second subplot
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('cos(x)')

# Third subplot
axs[1, 0].plot(x, y3)
axs[1, 0].set_title('log(x)')

# Fourth subplot
axs[1, 1].plot(x, y4)
axs[1, 1].set_title('exp(-x)')

# Adjust the spacing between subplots
fig.tight_layout()

# Show the plot
plt.show()
