# random number 1
import numpy as np

np.random.seed(123)
print(np.random.rand())

# random number 2
import numpy as np
np.random.seed(123)

dice_roll1 = np.random.randint(1, 7)
print("First dice roll:", dice_roll1)

dice_roll2 = np.random.randint(1, 7)
print("Second dice roll:", dice_roll2)

# random number 3
import numpy as np
np.random.seed(123)

step = 50

dice = np.random.randint(1, 7)

if dice <= 2:
    step = step - 1
elif 3 <= dice <= 5:
    step = step + 1
else:
    step = step + np.random.randint(1, 7)

print("Dice Roll:", dice)
print("Current Step:", step)

# random walk 1
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)
print(random_walk)

# random walk 2
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0,step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)
print(random_walk)

# visualize the walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

import matplotlib.pyplot as plt

plt.plot(random_walk)
plt.show()
