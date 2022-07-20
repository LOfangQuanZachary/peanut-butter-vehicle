from classes import *

# accepts a list of integer tuples and returns a list of tuples
# the tuples represent angle of the wheel and the distance to travel
# returns an array of int tuples containing angle and distance
def get_instructions_for_bezier(p0: Point, p1: Point, p2: Point, p3: Point, previewDistance: float, carLength: float) -> list:
    assert (1/previewDistance) % 1 == 0

    t = 0
    instructions = []

    # iterate from 0 to 1 stepping by previewDistance
    while t <= 1-previewDistance:
        x0, x1, x2, x3 = p0.x, p1.x, p2.x, p3.x
        y0, y1, y2, y3 = p0.y, p1.y, p2.y, p3.y

        c1x = (1-t)*((1-t)*x0+t*x1)+t*((1-t)*x1+t*x2)
        c1y = (1-t)*((1-t)*y0+t*y1)+t*((1-t)*y1+t*y2)
        c2x = (1-t)*((1-t)*x1+t*x2)+t*((1-t)*x2+t*x3)
        c2y = (1-t)*((1-t)*y1+t*y2)+t*((1-t)*y2+t*y3)

        # final coordinates of point c at t
        cx = (1-t)*c1x+t*c2x
        cy = (1-t)*c1y+t*c2y

        o = t + previewDistance

        d1x = (1-o)*((1-o)*x0+o*x1)+o*((1-o)*x1+o*x2)
        d1y = (1-o)*((1-o)*y0+o*y1)+o*((1-o)*y1+o*y2)
        d2x = (1-o)*((1-o)*x1+o*x2)+o*((1-o)*x2+o*x3)
        d2y = (1-o)*((1-o)*y1+o*y2)+o*((1-o)*y2+o*y3)

        # final coordinates of point d at o
        dx = (1-o)*d1x+o*d2x
        dy = (1-o)*d1y+o*d2y

        # find where the line perpendicular to c1 intersects the line perpendicular to the point between c1 and c2
        c_gradient = -1/((c1y-c2y)/(c1x-c2x))
        midgradient = -1/((cy-dy)/(cx-dx))
        midx_offset = (cx+dx)/-2
        midy_offset = (cy+dy)/2
        circle_x = ((midgradient*midx_offset+midy_offset)-(c_gradient*(-cx)+cy))/(c_gradient-midgradient)
        circle_y = circle_x*c_gradient + c_gradient*(-cx)+cy

        # find the distance from the intersection to point t
        distance = math.sqrt((circle_x-cx)**2+(circle_y-cy)**2)

        # find the angle and distance to travel on the circle defined by the intersection point and the radius
        angle_to_travel = math.atan(carLength/distance)
        distance_to_travel = abs(angle_between_points(Point(cx, cy), Point(dx, dy), distance, Point(circle_x, circle_y)) * distance)

        instructions.append((angle_to_travel, distance_to_travel))

        t += previewDistance
    
    return instructions

def sigmoid(x: float):
    if x >= 0: return 1
    else: return -1

def angle_between_points(p1: Point, p2: Point, radius: float, origin: Point) -> float:
    x1, y1 = p1.x-origin.x, p1.y-origin.y
    x2, y2 = p2.x-origin.x, p2.y-origin.y
    p = sigmoid(y1)*2*numpy.arcsin(math.sqrt((x1-radius)**2+(y1)**2)/(2*radius))
    d = sigmoid(y2)*2*numpy.arcsin(math.sqrt((x2-radius)**2+(y2)**2)/(2*radius))
    s = math.pi*(sigmoid((p-d-math.pi)*-1)+1)
    q = math.pi*(sigmoid((d-p-math.pi)*-1)+1)
    return (p+s)-(d+q)

for angle, distance in get_instructions_for_bezier(Point(5, 4), Point(19, 5), Point(7, 12), Point(20, 12), 0.1, 5.0):
    print(angle, distance)