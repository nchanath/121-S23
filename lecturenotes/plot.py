import numpy as np
import matplotlib.pyplot as plt

# Create an array of values for n ranging from 0 to 10000000
#n = np.arange(0, 10000)
n = np.arange(0, 100000)

# Calculate the values of the functions
y1 = 0.001 * n ** 3
y2 = 100000 * n

# Create the plot
plt.plot(n, y1, label='0.001n^3')
plt.plot(n, y2, label='100000n')

# Set the x and y axis labels and title
plt.xlabel('n')
plt.ylabel('y')
plt.title('Functions 0.001n^3 and 100000n')

# Add a legend to the plot
plt.legend()

# Show the plot
plt.show()
