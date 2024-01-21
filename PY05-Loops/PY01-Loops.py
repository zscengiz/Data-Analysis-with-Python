# while loop 1
offset = 8

while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)

# while loop 2
offset = -6

while offset != 0:
    print("correcting...")
    if offset > 0:
        offset = offset - 1
    else:
        offset = offset + 1
    print(offset)

# for loop 1
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

for i in areas :
    print(i)

# for loop 2
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

for index, a in enumerate(areas):
    print("room " + str(index) + ": " + str(a))

# for lop 3
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]

for room in house:
    print(room[0] + " is " + str(room[1]) + " sqm")

# for loop 4
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
for key, value in europe.items() :
    print("the capital of "+ key +" is "+ str(value))

# for loop 5
import numpy as np
np_height = [1.80, 2.15, 2.10, 2.10, 1.88, 1.76, 2.09, 2.00]
np_baseball = [180, 215, 210, 210, 188, 176, 209, 200]

for x in np_height :
    print(str(x) + " inches")

for i in np.nditer(np_baseball) :
    print(i)

# for loop 6
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

for label, row in cars.iterrows():
    print(label)
    print(row)

# for loop 7
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

for lab, row in cars.iterrows():
    print(lab + ": " + str(row["cars_per_cap"]))

# for loop 8
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

print(cars)
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

cars['COUNTRY'] = cars['country'].apply(str.upper)

print(cars)