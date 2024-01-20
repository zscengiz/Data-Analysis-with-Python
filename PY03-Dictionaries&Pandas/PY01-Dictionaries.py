#example 1
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany'
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger]) # berlin

#example 2
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid','france':'paris','germany':'berlin','norway':'oslo' }

# Print europe
print(europe) # {'norway': 'oslo', 'germany': 'berlin', 'spain': 'madrid', 'france': 'paris'}

#example 3
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys()) # dict_keys(['spain', 'france', 'germany', 'norway'])

# Print out value that belongs to key 'norway'
print(europe['norway']) # oslo