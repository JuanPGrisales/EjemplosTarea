



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

verts =20
num_cluster =5
diameter=100

points = fillWithPoints(verts, diameter**2)

numberPoints = len(points)
iterations = 3

pointsArray =  np.array(points)
groups = np.zeros(numberPoints)
# initialize clusters by picking num_cluster random points
# could improve on this by deliberately choosing most different points
for t in range(iterations):
    if t == 0:
        index_ = np.random.choice(range(numberPoints),num_cluster,replace=False)
        mean = pointsArray[index_]
    else:
        for k in range(num_cluster):
            mean[k] = np.mean(pointsArray[groups==k], axis=0)
    for i in range(numberPoints):
        dist = np.sum((mean - pointsArray[i])**2, axis=1)
        pred = np.argmin(dist)
        groups[i] = pred

for k in range(num_cluster):
    if(steps):
        fig = plt.scatter(pointsArray[groups==k,0], pointsArray[groups==k,1])


full = verts.append(tuple(verts[0]))
xs, ys = zip(*verts) #create lists of x and y values


if(steps):
    plt.plot(xs,ys,'b') 

_clusterPoints = [[] for _ in range(num_cluster)]
_clusterCenters = [(0,0) for _ in range(num_cluster)]
for i, _point in enumerate(pointsArray):
    _clusterPoints[int(groups[i])].append(_point)
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
    pointsArray = p.intersection(q)
    intersectPoly = pointsArray



    if(steps):
        xs = intersectPoly.exterior.coords.xy[0]
        ys = intersectPoly.exterior.coords.xy[1]
        plt.plot(xs,ys) 



    finalRegions.append(intersectPoly)
    

if(steps):
    plt.plot(points[:,0], points[:,1], 'ko')
return finalRegions



























#paintPoligon(verts, points)