#HISTOGRAM
# example 1
import matplotlib.pyplot as plt

life_exp = [75, 82, 68, 89, 78, 93, 70, 85, 79, 91]

# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()

# example 2
# Sample life expectancy data
life_exp = [75, 82, 68, 89, 78, 93, 70, 85, 79, 91]

# Build a histogram with 5 bins
plt.hist(life_exp, bins=5)

# Display the first histogram
plt.show()
plt.clf()  # Clean up for a fresh plot

# Build another histogram with 20 bins
plt.hist(life_exp, bins=20)

# Display the second histogram
plt.show()
