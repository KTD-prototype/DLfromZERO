import numpy as np
import matplotlib.pyplot as plt

# prepare data
x = np.arange(0, 6, 0.1)  # prepare data from 0 to 6 at resolution:0.1
y1 = np.sin(x)
y2 = np.cos(x)

# plot a graph
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")  # plot at broken line
plt.xlabel("x")  # label for x axis
plt.ylabel("y")  # label for y axis
plt.title('sin & cos')  # title of the graph
plt.legend()
plt.show()
