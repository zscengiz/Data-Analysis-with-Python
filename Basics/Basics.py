# Hello World
print('Hello World')

# Addition
print(4 + 5)

# Subtraction
print(5 - 5)

# Multiplication
print(3 * 5)

# Division
print(10 / 2)

# VARIABLES AND TYPES
height = 1.79
weight = 68.7
bmi = weight / height ** 2
print(bmi)
type(bmi) # float
x = "Sude" # str
y = True # bool
print(2 + 3)
print('ab' + 'ac') # abac

# str()
savings = 100
total_savings = 150
print("I started with $" + str(savings) + " and now have $" + str(total_savings) + ". Awesome!")
print("I can add integers, like " + str(5) + " to strings.")
print("I said " + ("Hey " * 2) + "Hey!")

# LISTS
fam = ["dad",1.73, 1.68, 1.84, 1.92]
fam2 = [["liz",1.73],
        ["emma",1.68],
        ["sue",1.84]]
print(fam2)

#
hall = 11.25
kit = 18.0
liv = 20.0
areas = [hall, kit, liv]
print(areas)

# Subsetting List
print(fam[0])
print(fam[1])
print(fam[2:5]) # [start : end]

# slice
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
eat_sleep_area = areas[3] + areas[7]
print(eat_sleep_area)
downstairs = areas[:6]
upstairs = areas[6:]

#
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]
bathroom_area = house[-1][1] # 9.50
print(house[1][1])
house[1][1] = 2
print(house[1][1])

# add item
areas_1 = areas + ["poolhouse", 24.5]
areas_2 = areas_1 + ["garage", 15.45]
print("Original areas list:", areas)
print("Extended areas with poolhouse:", areas_1)
print("Further extended areas with garage:", areas_2)

areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = areas[:]
areas_copy[0] = 5.0
print(areas) # [11.25, 18.0, 20.0, 10.75, 9.5]
print(areas_copy) # [5.0, 18.0, 20.0, 10.75, 9.5]

# FUNCTIONS
fam3 = [1.73, 1.68, 1.71, 1.89]
print(max(fam3)) # 1.89
tallest = max(fam3)
print(tallest) # 1.89

print(round(1.68, 1)) # 1.7
print(round(1.68)) # 2.0

print(len(fam3))

# sort
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

full = first + second

full_sorted1 = sorted(full)
full_sorted2 = sorted(full, reverse = True)
print(full.reverse())

print(full_sorted1) # [9.5, 10.75, 11.25, 18.0, 20.0]
print(full_sorted2) # [20.0, 18.0, 11.25, 10.75, 9.5]

# METHODS
arr = ["liz",1.73,"emma",1.68,"sue",1.84,1.68]
print(arr.index("liz")) # 0
print(arr.count(1.68)) # 2
print(arr.count(1.73)) # 1

sister = "liz"
print(sister.capitalize()) # Liz
print(sister.replace("z","sa")) # lisa
print(sister.replace("liz","sue")) # sue
print(sister.index("z")) # 2

# append and delete
new_item = ["me",1.68]
house.append(new_item) # [['hallway', 11.25], ['kitchen', 2], ['living room', 20.0], ['bedroom', 10.75], ['bathroom', 9.5], ['me', 1.68]]
print(house)
del(house[1])
print(house) # [['hallway', 11.25], ['living room', 20.0], ['bedroom', 10.75], ['bathroom', 9.5], ['me', 1.68]]

place = "poolhouse"
print(place.upper()) # POOLHOUSE
print(place.count("o")) # 3

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

# numpy
import numpy as np
baseball = [180, 215, 210, 210, 188, 176, 209, 200]
np_baseball = np.array(baseball)
print(type(np_baseball)) # <class 'numpy.ndarray'>

#
import numpy as np
np_height_in = np.array(height_in)
print(np_height_in)
np_height_m = np_height_in * 0.0254
print(np_height_m)

#
import numpy as np
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2
print(bmi)
