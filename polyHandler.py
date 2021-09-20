import random, math
from shapely.geometry import Polygon, Point, MultiPoint
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi
steps = False

def get_random_point_in_polygon(p):
    poly = Polygon(p)
    minx, miny, maxx, maxy = poly.bounds
    while True:
        p = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if poly.contains(p):
            return p

def generatePolygon(aveRadius=50,numVerts=20, ctrX=0, ctrY=0, irregularity=0.5, spikeyness=0.5) :
    irregularity = clip( irregularity, 0,1 ) * 2*math.pi / numVerts
    spikeyness = clip( spikeyness, 0,1 ) * aveRadius

    # generate n angle steps
    angleSteps = []
    lower = (2*math.pi / numVerts) - irregularity
    upper = (2*math.pi / numVerts) + irregularity
    sum = 0
    for i in range(numVerts) :
        tmp = random.uniform(lower, upper)
        angleSteps.append( tmp )
        sum = sum + tmp

    # normalize the steps so that point 0 and point n+1 are the same
    k = sum / (2*math.pi)
    for i in range(numVerts) :
        angleSteps[i] = angleSteps[i] / k

    # now generate the points
    points = []
    angle = random.uniform(0, 2*math.pi)
    for i in range(numVerts) :
        r_i = clip( random.gauss(aveRadius, spikeyness), 0, 2*aveRadius )
        x = ctrX + r_i*math.cos(angle)
        y = ctrY + r_i*math.sin(angle)
        points.append( (int(x),int(y)) )

        angle = angle + angleSteps[i]

    return points

def clip(x, min, max) :
    if( min > max ) :  return x    
    elif( x < min ) :  return min
    elif( x > max ) :  return max
    else :             return x

def paintPoligons(polys):
    for poly in polys:
        xs = Polygon(poly).exterior.coords.xy[0]
        ys = Polygon(poly).exterior.coords.xy[1]
        plt.plot(xs,ys)
    plt.show()

def fillWithPoints(poly, points):
    _list = []
    for i in range(points):
        pnt = get_random_point_in_polygon(poly)
        _list.append([pnt.x,pnt.y])
    return _list

def voronoi_finite_polygons_2d(vor, radius=None):
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

    return new_regions, np.asarray(new_vertices)

def splitPolygon(verts, num_cluster, diameter=100):

    points = fillWithPoints(verts, diameter**2)
    DIM = 2
    N = len(points)
    iterations = 3

    x =  np.array(points)
    y = np.zeros(N)
    # initialize clusters by picking num_cluster random points
    # could improve on this by deliberately choosing most different points
    for t in range(iterations):
        if t == 0:
            index_ = np.random.choice(range(N),num_cluster,replace=False)
            mean = x[index_]
        else:
            for k in range(num_cluster):
                mean[k] = np.mean(x[y==k], axis=0)
        for i in range(N):
            dist = np.sum((mean - x[i])**2, axis=1)
            pred = np.argmin(dist)
            y[i] = pred

    for k in range(num_cluster):
        if(steps):
            fig = plt.scatter(x[y==k,0], x[y==k,1])


    full = verts.append(tuple(verts[0]))
    xs, ys = zip(*verts) #create lists of x and y values


    if(steps):
        plt.plot(xs,ys,'b') 

    _clusterPoints = [[] for _ in range(num_cluster)]
    _clusterCenters = [(0,0) for _ in range(num_cluster)]
    for i, _point in enumerate(x):
        _clusterPoints[int(y[i])].append(_point)
    for i in range(num_cluster):
        _x = [p[0] for p in _clusterPoints[i]]
        _y = [p[1] for p in _clusterPoints[i]]
        centroid = (sum(_x) / len(_x), sum(_y) / len(_y))
        _clusterCenters[i] = centroid
        if(steps):
            plt.plot(centroid[0],centroid[1],'yx') 







    points = np.array(_clusterCenters)

    vor = Voronoi(points)

    regions, vertices = voronoi_finite_polygons_2d(vor,diameter*1.4)

    pts = MultiPoint([Point(i) for i in points])
    mask = pts.convex_hull
    new_vertices = []
    finalRegions = []
    for region in regions:
        polygon = vertices[region]
        #shape = list(polygon.shape)
        #shape[0] += 1
        #p = Polygon(np.append(polygon, polygon[0]).reshape(*shape)).intersection(mask)
        #poly = np.array(list(zip(p.boundary.coords.xy[0][:-1], p.boundary.coords.xy[1][:-1])))
        #new_vertices.append(poly)
        if(steps):
            plt.fill(*zip(*polygon), alpha=0.4)
        ###############find intersection
        _sectionAreaPoly = polygon
        _fullPoly = np.array([list(x) for x in verts])




        p = Polygon(_sectionAreaPoly)
        q = Polygon(_fullPoly)
        x = p.intersection(q)
        intersectPoly = x



        if(steps):
            xs = intersectPoly.exterior.coords.xy[0]
            ys = intersectPoly.exterior.coords.xy[1]
            plt.plot(xs,ys) 



        finalRegions.append(intersectPoly)
        

    if(steps):
        plt.plot(points[:,0], points[:,1], 'ko')
    return finalRegions




#polyMap = generatePolygon()
#splitPolys = splitPolygon(polyMap, 4)
#paintPoligons(splitPolys)























#paintPoligon(verts, points)