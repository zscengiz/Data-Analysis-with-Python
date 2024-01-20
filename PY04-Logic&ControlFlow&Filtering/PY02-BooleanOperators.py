# example 1
my_kitchen = 18.0
your_kitchen = 14.0

print(my_kitchen > 10 and my_kitchen < 18) # False
print(my_kitchen < 14 or my_kitchen > 17) # True
print(my_kitchen * 2 < your_kitchen * 3) # True

# example 2
import numpy as np

my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

print(np.logical_or(my_house > 18.5, my_house < 10))
print(np.logical_and(my_house< 11, your_house < 11))