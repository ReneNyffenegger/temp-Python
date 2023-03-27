import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# Define the latitude and longitude coordinates of the cities
cities = {
    'London': (-0.1276, 51.5072),
    'Zurich': (8.5417, 47.3769),
    'Yakutsk': (129.6759, 62.0355),
    'Natal': (-35.2009, -5.7793),
    'Nuuk': (-51.7214, 64.1836)
}

# Create a new figure with an Orthographic projection centered on the middle of the city locations
lon_0 = sum([lon for lon, lat in cities.values()]) / len(cities)
lat_0 = sum([lat for lon, lat in cities.values()]) / len(cities)
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Orthographic(central_longitude=lon_0, central_latitude=lat_0))

# Add coastlines and borders to the plot
ax.add_feature(ccrs.cartopy.feature.LAND)
ax.add_feature(ccrs.cartopy.feature.OCEAN)
ax.add_feature(ccrs.cartopy.feature.COASTLINE)
ax.add_feature(ccrs.cartopy.feature.BORDERS, linestyle=':')

# Plot the city markers and labels
for city, (lon, lat) in cities.items():
    pass
#   ax.scatter(lon, lat, transform=ccrs.Orthographic(), label=city, zorder=10)
#   ax.text(lon + 2, lat + 2, city, transform=ccrs.PlateCarree(), fontsize=8)

# Add a legend and title to the plot
ax.legend(loc='lower left')
ax.set_title('Map with Coastlines and City Markers')

# Show the plot
plt.show()
