import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

red_patch  = mpatches.Patch(color='red'  , label='The red data')
blue_patch = mpatches.Patch(color='blue' , label='Blue marble' )
g          = mpatches.Patch(color='green', label='Green beans' )

ax.legend(handles=[red_patch, blue_patch, g])

plt.show()
plt.waitforbuttonpress()

