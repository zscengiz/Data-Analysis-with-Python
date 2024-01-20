# example 1
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add Italy to europe
europe.update({'italy': 'rome'})

# Print out Italy in europe
print('italy' in europe)

# Add Poland to europe
europe.update({'poland': 'warsaw'})

# Print europe
print(europe)

# different way of example 1
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add Italy to europe
europe['italy'] = 'rome'

# Print out 'italy' in europe
print('italy' in europe)

# Add Poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)

# example 2
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe.update({'germany':'berlin'})

# Remove australia
del(europe['australia'])

print(europe)

# example 3
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital': 'rome', 'population': 59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

print(europe)