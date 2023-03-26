# import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt


cities = {
    'London' : (51.5072,  -0.1276),
    'Zurich' : (47.3769,   8.5417),
    'Yakutsk': (62.0355, 129.6759),
    'Natal'  : (-5.7793, -35.2009),
    'Nuuk'   : (64.1836, -51.7214)
}

prj = ccrs.Orthographic(central_latitude=47, central_longitude=9)

# Create a new figure with an Orthographic projection
fig = plt.figure(figsize=(8, 8))
# ax = fig.add_subplot(1, 1, 1, projection=ccrs.Orthographic(                                        ))
ax   = fig.add_subplot(1, 1, 1, projection=prj)

# Add coastlines to the plot
ax.coastlines()

ax.add_feature(ccrs.cartopy.feature.LAND)
ax.add_feature(ccrs.cartopy.feature.OCEAN)
ax.add_feature(ccrs.cartopy.feature.COASTLINE)
ax.add_feature(ccrs.cartopy.feature.BORDERS, linestyle=':')


# a   = np.array([ 80.0,  30.0])
# b   = np.array([100.0,  50.0])
# m   = np.array([ 60.0,  55.0])
# h   = np.array([ 64.0,  55.0])
# p   = np.array([ 70.0,  45.0])
# 
# points          = [a, b, p, m, h]
# point_names     = ['A', 'B', 'P', 'M', 'H']
# point_colors    = ['k', 'k', 'k', 'r', 'r']
# point_label_xy  = [(-10, -10), (10, 10), (-10, 5), (10, -5), (10, -3)]
# 
# lines           = [[a, b], [p, m]]
# line_colors     = ['k', 'r']
# 
# for point, color, name, label_xy in zip(
#         points, point_colors, point_names, point_label_xy):
# 
#     ax.scatter( point[0], point[1],
#                 color       = color,
#                 marker      = '.'
#               # latlon      = True
#                 )
# 
#   plt.annotate(   name,
#                   xy          = (point[0], point[1]),
#                   xycoords    = 'data',
#                   xytext      = label_xy,
#                   textcoords  = 'offset points',
#                   color       = color)



# for city, (lat, lon) in cities.items():
# #  ax.scatter(lon, lat, transform=prj, label=city)
#    ax.scatter(lon, lat,                label=city)

# Set the title of the plot
ax.set_title('Map with some cities')

# Show the plot
plt.show()

