# NumPy
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

#2D NumPy Arrays
import numpy as np
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
np_baseball = np.array(baseball)
print(type(np_baseball))
print(np_baseball.shape) # (4, 2) (columns, rows)

#NumPy: Basic Statistics
import numpy as np
np_height_in = np_baseball[:, 0]
print("Mean Height:", np.mean(np_height_in)) # The mean is obtained by dividing the sum of all values ​​in a data set by the number of elements.
print("Median Height:", np.median(np_height_in)) # The median is the middle value when a data set is ordered from smallest to largest.

#
import numpy as np
# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))
# Print median height
med = np.median(np_baseball[:,0])
print("Median: " + str(med))
# Print out the standard deviation on height. (A measure of the amount of variation or dispersion in a set of values.)
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))
# Print out correlation between first and second column. (A statistical measure that describes the extent to which two variables change together.)
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))

#  
import numpy as np
# Assume positions and heights are the given lists
# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)
# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']
# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']
print("Median height of goalkeepers: " + str(np.median(gk_heights)))
print("Median height of other players: " + str(np.median(other_heights)))





