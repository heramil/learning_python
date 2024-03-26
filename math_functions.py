# Modules and build-in fucntions for mathematical functions

import math

# BUILT-IN FUNCTIONS

x = 3.14
y = 4
z = 5
result = abs(y)
result = max(x, y, z)
result = min(x, y, z)
result = pow(4, 3)
result = round(x)
print(result)

# MODULE - CONSTANTS

print(math.pi)
print(math.e)

# MODULE - NUMBER-THEORETIC & REPRESENTATION FUNCTIONS

x = 9.9
result = math.sqrt(x)
result = math.ceil(x)
result = math.floor(x)
print(result) 

# EXAMPLE 1

a = float(input('Enter side A: '))
b = float(input('Enter side B: '))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f'Side C = {round(c, 2)}')

# EXAMPLE 2

radius = float(input('Enter the radius of a cirlce: '))
area = math.pi * pow(radius, 2)
print(f'The area of the circle is: {round(area, 2)} cm^2') 

# EXAMPLE 3

radius = float(input('Enter the radius of a cirlce: '))
circumference = 2 * math.pi * radius
print(f'The circumference is {round(circumference, 2)} cm') 


