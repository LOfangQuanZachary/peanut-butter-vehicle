from classes import *

# accepts a list of integer tuples and returns a list of tuples
# the tuples represent angle of the wheel and the distance to travel
# returns an array of int tuples containing angle and distance
def get_instructions_for_bezier(p0: Point, p1: Point, p2: Point, p3: Point, previewDistance: float):
    assert (1/previewDistance) % 1 == 0

    t = 0

    # iterate from 0 to 1 stepping by previewDistance
    while t <= 1-previewDistance:
        x0, x1, x2, x3 = p0.x, p1.x, p2.x, p3.x
        y0, y1, y2, y3 = p0.y, p1.y, p2.y, p3.y

        c1x = (1-t)*((1-t)*x0+t*x1)+t*((1-t)*x1+t*x2)
        c1y = (1-t)*((1-t)*y0+t*y1)+t*((1-t)*y1+t*y2)
        c2x = (1-t)*((1-t)*x1+t*x2)+t*((1-t)*x2+t*x3)
        c2y = (1-t)*((1-t)*y1+t*y2)+t*((1-t)*y2+t*y3)

        gradient = (c2y-c1y)/(c2x-c1x)

        angle = math.atan(gradient) * 180 / math.pi
        
        print(gradient, "\n\t", angle)
        t += previewDistance

get_instructions_for_bezier(Point(5, 4), Point(19, 5), Point(7, 12), Point(20, 12), 0.1)