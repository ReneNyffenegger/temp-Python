#
#   https://stackoverflow.com/questions/53195551/cartopy-plotting-points-incorrectly-with-orthographic-projection
#
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# create the lat/lon points
lons = np.array([214.5, 2.7, 197.5])
lats = np.array([35, 36, 37.])

# create the projections
ortho = ccrs.Orthographic(central_longitude=0, central_latitude=90)
geo = ccrs.Geodetic()

# create the geoaxes for an orthographic projection
ax = plt.axes(projection=ortho)

# plot native orthographic scatter points                                                                                
ax.scatter(lons, lats, marker='o', c='r', transform=geo)

# plot north pole for reference                                                                                               
# plot north pole for reference (with a projection transform)                                                                                           
ax.plot([0], [90], 'b^', transform=geo)

# add coastlines for reference                                                                                                
ax.coastlines(resolution='50m')
ax.set_global()

plt.show()
