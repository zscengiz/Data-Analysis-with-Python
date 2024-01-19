#Line Plot example 1
# Import the matplotlib.pyplot module
import matplotlib.pyplot as plt

# Define the Year (year) and Population (pop) lists
year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2100]
pop = [2.5, 3.0, 3.7, 4.2, 5.2, 6.1, 7.0, 7.8, 8.5, 9.1, 9.7, 10.9]

# Print the last year in the dataset and the predicted population for the year 2100
print("Last year in the dataset:", year[-1])
print("Predicted population for the year 2100:", pop[-1])

# Create a line plot: x-axis as year, y-axis as pop
plt.plot(year, pop)

# Add a title to the plot
plt.title('Line Plot Example 1')

# Display the plot
plt.show()

#Line Plot example 2
life_exp = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2100]
gdp_cap = [2.5, 3.0, 3.7, 4.2, 5.2, 6.1, 7.0, 7.8, 8.5, 9.1, 9.7, 10.9]

# Print the last item from both lists
print("The last item of gdp_cap:", gdp_cap[-1])
print("The last item of life_exp:", life_exp[-1])

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap, life_exp)

# Add a title to the plot
plt.title('Relationship between GDP per Capita and Life Expectancy (2007)')

# Display the plot
plt.show()
