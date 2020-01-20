import numpy as np
import matplotlib.pyplot as plt

# prepare data
x = np.arange(0, 6, 0.1)  # prepare data from 0 to 6 at resolution:0.1
y = np.sin(x)

# plot a graph
plt.plot(x, y)
plt.show()
