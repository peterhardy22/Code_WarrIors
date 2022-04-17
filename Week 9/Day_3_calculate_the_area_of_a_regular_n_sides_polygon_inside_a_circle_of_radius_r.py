
# https://www.codewars.com/kata/5a58ca28e626c55ae000018a
# Level 6 kyu

# Directions:
# Write the following function:
# def area_of_polygon_inside_circle(circle_radius, number_of_sides):
# It should calculate the area of a regular polygon of numberOfSides, number-of-sides, or number_of_sides sides inside a circle of radius circleRadius, circle-radius, or circle_radius which passes through all the vertices of the polygon (such circle is called circumscribed circle or circumcircle). 
# The answer should be a number rounded to 3 decimal places.
# Input :: Output Examples
# area_of_polygon_inside_circle(3, 3) # returns 11.691
# area_of_polygon_inside_circle(5.8, 7) # returns 92.053
# area_of_polygon_inside_circle(4, 5) # returns 38.042


# Function
def area_of_polygon_inside_circle(circle_radius, number_of_sides):
    from math import sin, cos, radians
    # Perform calculations for end equation.
    angle: float = radians(360 / (number_of_sides * 2))
    opposite_side: float = circle_radius * sin(angle)
    adjacent_side: float = circle_radius * cos(angle)
    
    return round(adjacent_side * opposite_side * number_of_sides, 3)


# Test Cases
test.describe('Example Tests')
test.it('ex1')
test.assert_equals(area_of_polygon_inside_circle(3, 3), 11.691)
test.it('ex2')
test.assert_equals(area_of_polygon_inside_circle(2, 4), 8)
test.it('ex3')
test.assert_equals(area_of_polygon_inside_circle(2.5, 5), 14.86)