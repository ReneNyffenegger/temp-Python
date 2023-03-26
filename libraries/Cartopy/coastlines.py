import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# Create a new figure with a Cartopy projection
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

# Add coastlines to the plot
ax.coastlines()

# Set the title of the plot
ax.set_title('Map with Coastlines')

# Show the plot
plt.show()
