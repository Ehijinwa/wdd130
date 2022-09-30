import math

length = float(input("what is the length of a side of the square"))
square = length ** 2
print(f"the area of the square is {square}")
length = float(input("what is the length of the rectangle"))
width = float(input("what is the width of the rectangle"))
area = length * width 
print(f"the area of the rectangle is {area}")
length = float(input("what is the radius of the circle"))
area = math.pi * (length ** 2)
print(f"the area of the circle is {area}")
length = float(input("what is the length"))
area_square = length ** 2
area_circle =math.pi * (length ** 2)
volume_cube = length ** 3
volume_sphere = (4/3) * math.pi * (length ** 2)
print(f"the square area is {area_square}")
print(f"the circle area is {area_circle}")
print(f"the cube volume is {volume_cube}")
print(f"the sphere volume is {volume_sphere}")
