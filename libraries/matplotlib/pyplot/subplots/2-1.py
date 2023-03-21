#!/usr/bin/env python

import matplotlib.pyplot as plt

def example_plot(ax, faceColor):
    ax.plot([1, 2])
    ax.set_facecolor(faceColor)

    ax.locator_params(nbins=3)
    ax.set_xlabel('x-label', fontsize=11)
    ax.set_ylabel('y-label', fontsize=11)
    ax.set_title('Title'   , fontsize=11)


fig = plt.figure()

ax1 = plt.subplot(221)
ax2 = plt.subplot(223)
ax3 = plt.subplot(122)

example_plot(ax1, 'cornflowerblue')
example_plot(ax2, 'palegreen'     )
example_plot(ax3, 'khaki'         )

plt.tight_layout()

plt.show()
