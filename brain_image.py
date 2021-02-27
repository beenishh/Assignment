# navigate to the folder where the required image is saved
cd /mnt/c/Users/beenish/Downloads/
# activate conda environment
conda activate image_processing 
python

# read the image into a numpy.ndarray
import numpy as np 
import matplotlib.pyplot as plt 

brain_image=plt.imread("Brain.jpg") 
plt.imshow(brain_image)
plt.title('Display Image read using imread()') 
plt.axis('off')
plt.show()    # show the image as output

# find the dimension of the image
brain_image.shape

# use the reverse greyscale colormap 
plt.imshow(brain_image, cmap='Greys_r')
plt.show()    # show the image as output

# plot histogram of the image
plt.hist(brain_image, bins=10)
plt.show()   # show the image as output

# perform gaussian smoothing on the image 
from scipy import ndimage
level_1 = ndimage.gaussian_filter(brain_image, sigma=5)
plt.imshow(level_1)
plt.show()     # show the image as output

plt.imshow(level_1, cmap='Greys_r')      # use the reverse greyscale colormap for better viewing
plt.show()     # show the image as output

plt.hist(level_1, bins=10)
plt.show()    # show the image as output

# second level of gaussian smoothing
level_2 = ndimage.gaussian_filter(brain_image, sigma=10)
plt.imshow(level_2)

plt.imshow(level_2, cmap='Greys_r')     # use the reverse greyscale colormap
plt.show()

plt.hist(level_2, bins=10)
plt.show()       # show the image as output
