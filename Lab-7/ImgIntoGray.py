from skimage import io
from matplotlib import pyplot as plt
image = io.imread("ImgPy.png")

# plt.imshow(image[::10,::10])

r,g,b = image[::,::,0],image[::,::,1],image[::,::,2]

imgGray = 0.2989 * r + 0.5870 * b + 0.1140 * g

img = imgGray

plt.imshow(img , cmap="gray")

plt.show()