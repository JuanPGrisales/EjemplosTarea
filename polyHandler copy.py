import random, math
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point, MultiPoint, point
from scipy.spatial import Voronoi

_TRACE = False

def clip(x, min, max):
    if(min > max):
        return x
    elif(x < min):
        return min
    elif(x > max):
        return max
    return x

def randomPolygon(_numberVertices):
    # variables
    averageRadius = 0.5
    numberVertices = _numberVertices
    polygonCenter = Point(0, 0)
    irregularity = 0.5
    spikeyness = 0.5
    irregularity = clip(irregularity, 0, 1) * 2 * math.pi / numberVertices
    spikeyness = clip(spikeyness, 0, 1) * averageRadius

    # generate n angle steps
    angleSteps = []
    lower = (2 * math.pi / numberVertices) - irregularity
    upper = (2 * math.pi / numberVertices) + irregularity
    sum = 0
    for i in range(numberVertices):
        tmp = random.uniform(lower, upper)
        angleSteps.append(tmp)
        sum = sum + tmp

    # normalize the steps so that point 0 and point n+1 are the same
    k = sum / (2 * math.pi)
    for i in range(numberVertices):
        angleSteps[i] = angleSteps[i] / k

    # now generate the points
    points = []
    angle = random.uniform(0, 2 * math.pi)
    for i in range(numberVertices):
        r_i = clip( random.gauss(averageRadius, spikeyness), 0, 2 * averageRadius)
        x = polygonCenter.x + r_i * math.cos(angle)
        y = polygonCenter.y + r_i * math.sin(angle)
        points.append((x, y))
        angle = angle + angleSteps[i]
    return Polygon(points)

def kmeans(_points, _numberSectors):
    pointsList = [[point.x,point.y] for point in _points]
    pointsArray = np.array(pointsList)
    numberPoints = len(pointsArray)
    iterations = 3
    pointsSector = np.zeros(numberPoints)

    for t in range(iterations):
        if t == 0:
            index_ = np.random.choice(range(numberPoints), _numberSectors, replace=False)
            mean = pointsArray[index_]
        else:
            for k in range(_numberSectors):
                mean[k] = np.mean(pointsArray[pointsSector==k], axis=0)
        for i in range(numberPoints):
            dist = np.sum((mean - pointsArray[i])**2, axis=1)
            pred = np.argmin(dist)
            pointsSector[i] = pred
    sectors = [[] for _ in range(_numberSectors)]
    for index, sector in enumerate(pointsSector):
        sectors[int(sector)].append(_points[index])
    return sectors

def generatePolygonPoint(_polygon):
    minx, miny, maxx, maxy = _polygon.bounds
    while True:
        p = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if _polygon.contains(p):
            return p

def generatePolygonPoints(_polygon, _numberPoints):
    _points = []
    for _ in range(int(_numberPoints)):
        _points.append(generatePolygonPoint(_polygon))
    return _points

def splitPolygon(_polygon, _numberSectors):
    plt.cla()
    if(_TRACE):
        x = _polygon.exterior.coords.xy[0]
        y = _polygon.exterior.coords.xy[1]
        plt.plot(x, y)
    # create random points inside the polygon
    numberPoints = _polygon.area * 10000
    polygonPoints = generatePolygonPoints(_polygon, numberPoints)

    # run k-means clustering for the random points using the number of sectors as the amount of clusters
    pointsSectors = kmeans(polygonPoints, _numberSectors)
    if(_TRACE):
        for sector in pointsSectors:
            x = [p.x for p in sector]
            y = [p.y for p in sector]
            plt.scatter(x, y)

    # find the center of each cluster of points
    centers = [findCenter(sector) for sector in pointsSectors]
    if(_TRACE):
        x = [p.x for p in centers]
        y = [p.y for p in centers]
        plt.scatter(x, y)

    # find the voronoi polygons for the centroids
    voronoi = Voronoi(np.array([[p.x,p.y] for p in centers]))
    regions = voronoi_finite_polygons_2d(voronoi)


    # find the minimum bounding box around the polygon
    box = _polygon.minimum_rotated_rectangle
    if(_TRACE):
        x = box.exterior.coords.xy[0]
        y = box.exterior.coords.xy[1]
        plt.plot(x, y)
        

    # find the intersection between the veronoi polygons and the minimum bounding box
    subRegions = []
    for region in regions:
        intersectPoly = region.intersection(box)
        subRegions.append(intersectPoly)
        if(_TRACE):
            x = intersectPoly.exterior.coords.xy[0]
            y = intersectPoly.exterior.coords.xy[1]
            plt.plot(x, y)

    # find the intersection between the original polygon and voronoi polygons to find the sectors

    finalRegions = []
    for region in subRegions:
        intersectPoly = region.intersection(_polygon)
        finalRegions.append(intersectPoly)
        if(_TRACE):
            x = intersectPoly.exterior.coords.xy[0]
            y = intersectPoly.exterior.coords.xy[1]
            plt.plot(x, y)

    if(_TRACE):
        plt.show()
        plt.cla()

    for region in finalRegions: # try break it
        x = region.exterior.coords.xy[0]
        y = region.exterior.coords.xy[1]

    return finalRegions


def voronoi_finite_polygons_2d(vor, radius=1000):
    """
    Reconstruct infinite voronoi regions in a 2D diagram to finite
    regions.
    Parameters
    ----------
    vor : Voronoi
        Input diagram
    radius : float, optional
        Distance to 'points at infinity'.
    Returns
    -------
    regions : list of tuples
        Indices of vertices in each revised Voronoi regions.
    vertices : list of tuples
        Coordinates for revised Voronoi vertices. Same as coordinates
        of input vertices, with 'points at infinity' appended to the
        end.
    """

    if vor.points.shape[1] != 2:
        raise ValueError("Requires 2D input")

    new_regions = []
    new_vertices = vor.vertices.tolist()

    center = vor.points.mean(axis=0)
    if radius is None:
        radius = vor.points.ptp().max()

    # Construct a map containing all ridges for a given point
    all_ridges = {}
    for (p1, p2), (v1, v2) in zip(vor.ridge_points, vor.ridge_vertices):
        all_ridges.setdefault(p1, []).append((p2, v1, v2))
        all_ridges.setdefault(p2, []).append((p1, v1, v2))

    # Reconstruct infinite regions
    for p1, region in enumerate(vor.point_region):
        vertices = vor.regions[region]

        if all(v >= 0 for v in vertices):
            # finite region
            new_regions.append(vertices)
            continue

        # reconstruct a non-finite region
        ridges = all_ridges[p1]
        new_region = [v for v in vertices if v >= 0]

        for p2, v1, v2 in ridges:
            if v2 < 0:
                v1, v2 = v2, v1
            if v1 >= 0:
                # finite ridge: already in the region
                continue

            # Compute the missing endpoint of an infinite ridge

            t = vor.points[p2] - vor.points[p1] # tangent
            t /= np.linalg.norm(t)
            n = np.array([-t[1], t[0]])  # normal

            midpoint = vor.points[[p1, p2]].mean(axis=0)
            direction = np.sign(np.dot(midpoint - center, n)) * n
            far_point = vor.vertices[v2] + direction * radius

            new_region.append(len(new_vertices))
            new_vertices.append(far_point.tolist())

        # sort region counterclockwise
        vs = np.asarray([new_vertices[v] for v in new_region])
        c = vs.mean(axis=0)
        angles = np.arctan2(vs[:,1] - c[1], vs[:,0] - c[0])
        new_region = np.array(new_region)[np.argsort(angles)]

        # finish
        new_regions.append(new_region.tolist())

    vertices = np.asarray(new_vertices)
    regs = []
    for region in new_regions:
        regs.append(Polygon(vertices[region]))
    return regs

def findCenter(_sector):
        _x = [p.x for p in _sector]
        _y = [p.y for p in _sector]
        centroid = Point(sum(_x) / len(_x), sum(_y) / len(_y))
        return centroid

def drawObjects(_objects):
    for object in _objects:
        if(type(object).__name__ == "Polygon"):
            x = object.exterior.coords.xy[0]
            y = object.exterior.coords.xy[1]
            plt.plot(x, y)
        elif(type(object).__name__ == "Point"):
            plt.plot(object.x, object.y, 'ro')
        elif(type(object).__name__ == "List"):
            for object2 in _objects:
                if(type(object2).__name__ == "Polygon"):
                    x = object2.exterior.coords.xy[0]
                    y = object2.exterior.coords.xy[1]
                    plt.plot(x, y)
                elif(type(object2).__name__ == "Point"):
                    plt.plot(object2.x, object2.y, 'ro')
    plt.show()

# Start
# numberVertices = 20
# polygon = randomPolygon(numberVertices)
# numberSectors = 5
# polygonSectors = []
# 
# while(True):
#     try:
#         polygonSectors = splitPolygon(polygon, numberSectors)
#         break
#     except:
#         pass
# 
# for region in polygonSectors:
#     x = region.exterior.coords.xy[0]
#     y = region.exterior.coords.xy[1]
#     plt.plot(x, y)
# plt.show()
# End
