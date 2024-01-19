# PACKAGES
# Import the math package
import math
r = 0.43
C = 2 * math.pi * r
A = math.pi * r ** 2
print("Circumference: " + str(C))
print("Area: " + str(A))

#
from math import radians
r = 192500
phi = radians(12)
dist = r * phi
print(dist)

#
from scipy.linalg import inv as my_inv
matrix = [[1, 2], [3, 4]]
inverse_matrix = my_inv(matrix)
print(inverse_matrix)