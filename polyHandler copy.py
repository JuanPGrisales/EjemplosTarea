import random, math
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point, MultiPoint
from scipy.spatial import Voronoi

_TRACE = True









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

    polygon = Polygon(points)
    if(_TRACE):
        drawObjects([polygon])
    return polygon








def kmeans(_points, _numberSectors):
    pointsArray = np.array(_points)
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

    if(_TRACE):
        drawObjects(pointsSector)
    return pointsSector

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
    if(_TRACE):
        drawObjects(_points)
    return _points

def splitPolygon(_polygon, _numberSectors):
    # create random points inside the polygon
    numberPoints = _polygon.area * 1000
    polygonPoints = generatePolygonPoints(_polygon, numberPoints)

    # run k-means clustering for the random points using the number of sectors as the amount of clusters
    pointsSectors = kmeans(polygonPoints, _numberSectors)

    # find the center of each cluster of points

    # find the voronoi polygons for the centroids

    # find the minimum bounding box around the polygon
    box = _polygon.minimum_rotated_rectangle

    # find the intersection between the veronoi polygons and the minimum bounding box


    # find the intersection between the original polygon and voronoi polygons to find the sectors

    return [box,_polygon]

def drawObjects(_objects):
    for object in _objects:
        if(type(object).__name__ == "Polygon"):
            x = object.exterior.coords.xy[0]
            y = object.exterior.coords.xy[1]
            plt.plot(x, y)
        elif(type(object).__name__ == "Point"):
            plt.plot(object.x, object.y, 'ro')
    plt.show()






# Start
numberVertices = 20
polygon = randomPolygon(numberVertices)
numberSectors = 5
polygonSectors = splitPolygon(polygon, numberSectors)
drawObjects(polygonSectors)
# End