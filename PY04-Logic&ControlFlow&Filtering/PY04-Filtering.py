# example 1
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr]
print(sel)

# example 2
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
#dr = cars['drives_right']
#sel = cars[dr]
sel = cars[cars['drives_right']]

print(sel)

# example 3
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Create cpc: Pandas Series of cars_per_cap column
cpc = cars['cars_per_cap']

# Create many_cars: Boolean Series based on the condition cars_per_cap > 500
many_cars = cpc > 500

# Create car_maniac: Subset cars based on the condition many_cars
car_maniac = cars[many_cars]

print(car_maniac)

# example 4
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc >100, cpc < 500)
medium = cars[between]

print(medium)
