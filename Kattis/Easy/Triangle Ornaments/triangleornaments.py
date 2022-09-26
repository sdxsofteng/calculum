import sys
import math

first = True
split_triangles = list()
for i in sys.stdin:
    if first:
        number_of_triangles = int(i.strip("\n"))
        first = False
    else:
        split_triangles.append(i.strip("\n").split(" "))

for triangle in split_triangles:
    for i in range(len(triangle)):
        triangle[i] = int(triangle[i])

total_width = 0


for triangle in split_triangles:
    a,b,c = triangle
    angle_a = math.acos((b**2+c**2-a**2)/(2*b*c))
    m = math.sqrt((c/2)**2+b**2-b*c*math.cos(angle_a))
    s = c/2
    left_c = math.acos((a**2+m**2-s**2)/(2*a*m))
    side_1_parallelogram_area = a*m*math.sin(left_c)
    side_1_height = side_1_parallelogram_area / m
    right_c = math.acos((m**2+b**2-s**2)/(2*m*b))
    side_2_parallelogram_area = m*b*math.sin(right_c)
    side_2_height = side_2_parallelogram_area / m
    total_height = side_1_height + side_2_height
    total_width += total_height

print(total_width)