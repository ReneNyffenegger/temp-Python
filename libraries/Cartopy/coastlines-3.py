#
#   https://stackoverflow.com/questions/53195551/cartopy-plotting-points-incorrectly-with-orthographic-projection
#
# import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

cities = {
    'London' : (-0.1276, 51.5072),
    'Zurich' : (8.5417, 47.3769),
    'Yakutsk': (129.6759, 62.0355),
    'Natal'  : (-35.2009, -5.7793),
    'Nuuk'  : (-51.7214, 64.1836)
}

# create the lat/lon points
# lons = np.array([214.5, 2.7, 197.5])
# lats = np.array([35, 36, 37.])
# lons = [214.5, 2.7, 197.5]
# lats = [35   , 36 , 37.  ]

# create the projections
ortho = ccrs.Orthographic(central_longitude=cities['Zurich'][0], central_latitude=cities['Zurich'][1])
geo = ccrs.Geodetic()

# create the geoaxes for an orthographic projection
ax = plt.axes(projection=ortho)

# plot native orthographic scatter points                                                                                
# ax.scatter(lons, lats, marker='o', c='r', transform=geo)

for city, (lon, lat) in cities.items():
#   pass
#   ax.scatter(lon, lat, transform=ccrs.Orthographic(), label=city, zorder=10, marker = 'o', c='r')
    ax.scatter(lon, lat, transform=geo                , label=city, zorder=10, marker = 'o', c='r')
    ax.text(lon + 2, lat + 2, city, transform=ccrs.PlateCarree(), fontsize=8)

# plot north pole for reference                                                                                               
# plot north pole for reference (with a projection transform)                                                                                           
ax.plot([0], [90], 'b^', transform=geo)

# add coastlines for reference                                                                                                
ax.coastlines(resolution='50m')
ax.set_global()

plt.show()
