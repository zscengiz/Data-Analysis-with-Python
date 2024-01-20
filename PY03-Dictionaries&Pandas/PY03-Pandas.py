# example 1
# Import pandas as pd
import pandas as pd
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# example 2
import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

print("------------------------------------------------")

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

print(cars)

# example 3
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

print(cars)

# example 4
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col=0)

print(cars)

# example 5
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Select the first 3 observations from cars and print them out
print(cars[0:3])

# Select the fourth, fifth and sixth observation, corresponding to row indexes 3, 4 and 5, and print them out
print(cars[3:6])

# example 6
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame for Russia and Morocco, with columns country and drives_right
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

# example 7
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])
#cars.iloc[:, 2]

# Print out drives_right column as DataFrame
print(cars.loc[:,['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['cars_per_cap','drives_right']])
#cars.iloc[:, [0, 2]]