import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('lena.png')  # read a image (set appropriate pass)
plt.imshow(img)

plt.show()
