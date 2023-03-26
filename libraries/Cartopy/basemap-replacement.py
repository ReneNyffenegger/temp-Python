from geographiclib.geodesic import Geodesic
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature


def dist_from_great_circle_to_point(a, b, p):
    '''
    Calculates the shortest distance between a point P and a great
    circle passing through A and B. The method is:
        1. Find azimuth for line AP.
        2. Find azimuth for line AB.
        3. Consider point M which is the mirror image of point P
            in the great circle. Find azimuth AM from the first
            two azimuths.
        4. Find great circle between P and M. The point of interest
            is half-way along this line.

    Input
    a       [lon, lat] of first point defining the great circle.
    b       [lon, lat] of second point defining the great circle.
    p       [lon, lat] of query point.

    Output
    h       [lon, lat] on great circle closest to query point.
    d       Perpendicular distance between great circle and point.
    m       [lon, lat] of mirror image point.
    '''

    # Ellipsoid.
    ell     = Geodesic.WGS84

    # ab    Geodesic from A to B.
    # az_ab Azimuth of geodesic from A to B.
    ab      = ell.Inverse(a[1], a[0], b[1], b[0])
    az_ab   = ab['azi1']

    # ap    Geodesic from A to P.
    # az_ap Azimuth of geodesic from A to P.
    # d_p   Distance between A and P along geodesic.
    ap      = ell.Inverse(a[1], a[0], p[1], p[0])
    az_ap   = ap['azi1']
    d_ap    = ap['s12']

    # Point M is the image of P on the other side of line AB.
    # az_am Azimuth of geodesic from A to M.
    # am    Geodesic from A to M.
    # m     [lon, lat] of point M.
    az_am   = az_ab + (az_ab - az_ap)
    am      = ell.Direct(a[1], a[0], az_am, d_ap)
    m       = np.array([am['lon2'], am['lat2']])

    # Point H is the half-way between P and M along a great circle.
    # pm    Geodesic from P to M.
    # d     Half of the distance from P to M.
    # ph    Geodesic from P to H.
    # h     [lon, lat] of point H.
    pm      = ell.Inverse(p[1], p[0], m[1], m[0])
    d       = pm['s12']/2.0
    ph      = ell.Direct(p[1], p[0], pm['azi1'], d)
    h       = np.array([ph['lon2'], ph['lat2']])

    return h, d, m


def test():

    a = np.array([80.0, 30.0])
    b = np.array([100.0, 50.0])
    p = np.array([70.0, 45.0])
  #
  # https://stackoverflow.com/questions/50787840/distance-between-great-circle-and-point
  #
    h, d, m = dist_from_great_circle_to_point(a, b, p)

    print(h)
    
    fig = plt.figure()
    ax = plt.axes(projection=ccrs.Orthographic(central_longitude=85.0, central_latitude=35.0))
    ax.add_feature(cfeature.COASTLINE, linewidth=0.25)
    
    points = [a, b, p, m, h]
    point_names = ['A', 'B', 'P', 'M', 'H']
    point_colors = ['k', 'k', 'k', 'r', 'r']
    point_label_xy = [(-10, -10), (10, 10), (-10, 5), (10, -5), (10, -3)]
    
    lines = [[a, b], [p, m]]
    line_colors = ['k', 'r']
    
    for point, color, name, label_xy in zip(points, point_colors, point_names, point_label_xy):
        plt.scatter(point[0], point[1],
                    color=color,
                    marker='.',
                    transform=ccrs.PlateCarree())
    
        plt.annotate(name,
                     xy=(point[0], point[1]),
                     xycoords=ccrs.PlateCarree()._as_mpl_transform(ax),
                     xytext=label_xy,
                     textcoords='offset points',
                     color=color)
    
    for line, color in zip(lines, line_colors):
        ax.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]],
                color=color,
                lw=1,
                transform=ccrs.PlateCarree(),
                linestyle='--')
    
    plt.show()


test()
