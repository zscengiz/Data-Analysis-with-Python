# Scatter Plot example 1
# Import the matplotlib.pyplot module
import matplotlib.pyplot as plt

life_exp = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2100]
gdp_cap = [2.5, 3.0, 3.7, 4.2, 5.2, 6.1, 7.0, 7.8, 8.5, 9.1, 9.7, 10.9]

# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()