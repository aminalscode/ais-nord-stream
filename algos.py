# -------------------------------------------------------------------------------
# Source: https://github.com/sasamil/PointInPolygon_Py/blob/master/pointInside.py by https://github.com/sasamil
# This function gives the answer whether the given point is inside or outside the predefined polygon
# Unlike standard ray-casting algorithm, this one works on edges! (with no performance cost)
# According to performance tests - this is the best variant.

# arguments:
# Polygon - searched polygon
# Point - an arbitrary point that can be inside or outside the polygon
# length - the number of point in polygon (Attention! The list itself has an additional member
# - the last point coincides with the first)

# return value:
# 0 - the point is outside the polygon
# 1 - the point is inside the polygon
# 2 - the point is one edge (boundary)
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
# Customization for NS1 and NS2 boundary box detection
# NS1
# 55°34'43.52"N,  15°38'23.91"E or 55.578756, 15.639975
# 55°34'53.35"N,  15°50'24.88"E or 55.581486, 15.840244
# 55°30'28.29"N,  15°51'1.13"E or 55.507858, 15.850314
# 55°30'22.80"N,  15°38'31.49"E or 55.506333, 15.642081

# NS2
# 54°53'25.49"N, 15°23'2.84"E or 54.890414, 15.384122
# 54°53'27.87"N, 15°25'52.74"E or 54.891075, 15.431317
# 54°51'47.88"N, 15°26'1.47"E or 54.863300, 15.433742
# 54°51'47.36"N, 15°23'8.64"E or 54.863156, 15.385733

Rostock_polygon = [
    (54.1765903, 12.0921641),
    (54.1743043, 12.0946747),
    (54.1718802, 12.0961874),
    (54.1709571, 12.0967077),
    (54.1699335, 12.096756),
    (54.1681247, 12.1021204),
    (54.171987, 12.0998783),
    (54.1758493, 12.0975499),
    (54.1762889, 12.0956832),
    (54.1765903, 12.0921641),
]

NS1_polygon = [
    (55.578756, 15.639975),
    (55.581486, 15.840244),
    (55.507858, 15.850314),
    (55.506333, 15.642081),
    (55.578756, 15.639975),
]
NS2_polygon = [
    (54.890414, 15.384122),
    (54.891075, 15.431317),
    (54.863300, 15.433742),
    (54.863156, 15.385733),
    (54.890414, 15.384122),
]

NS1_large_polygon = [
    (55.70381, 15.37574),
    (55.72856, 16.09535),
    (55.3837, 16.11183),
    (55.36185, 15.37849),
    (55.70381, 15.37574),
]


def inside_rostock(point):
    return is_inside_sm(Rostock_polygon, point)


def inside_rostock_exit(point):
    return is_inside_sm(Rostock_polygon_exit, point)


def inside_ns1_large(point):
    return is_inside_sm(NS1_large_polygon, point)


def inside_ns1(point):
    return is_inside_sm(NS1_polygon, point)


def inside_ns2(point):
    return is_inside_sm(NS2_polygon, point)


# -------------------------------------------------------------------------------


def is_inside_sm(polygon, point):
    length = len(polygon) - 1
    dy2 = point[1] - polygon[0][1]
    intersections = 0
    ii = 0
    jj = 1

    while ii < length:
        dy = dy2
        dy2 = point[1] - polygon[jj][1]

        # consider only lines which are not completely above/bellow/right from the point
        if dy * dy2 <= 0.0 and (
            point[0] >= polygon[ii][0] or point[0] >= polygon[jj][0]
        ):
            # non-horizontal line
            if dy < 0 or dy2 < 0:
                F = dy * (polygon[jj][0] - polygon[ii][0]) / (dy - dy2) + polygon[ii][0]

                # if line is left from the point - the ray moving towards left, will intersect it
                if point[0] > F:
                    intersections += 1
                elif point[0] == F:  # point on line
                    return 2

            # point on upper peak (dy2=dx2=0) or horizontal line (dy=dy2=0 and dx*dx2<=0)
            elif dy2 == 0 and (
                point[0] == polygon[jj][0]
                or (
                    dy == 0
                    and (point[0] - polygon[ii][0]) * (point[0] - polygon[jj][0]) <= 0
                )
            ):
                return 2

        ii = jj
        jj += 1

    # print 'intersections =', intersections
    return intersections & 1
