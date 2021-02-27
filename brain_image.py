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
plt.show()     # show the image as output and realize that you need to use reverse greyscale colormap

plt.imshow(level_1, cmap='Greys_r')      # use the reverse greyscale colormap for better viewing
plt.show()     

plt.hist(level_1, bins=10)               # plot the histogram   
plt.show()    # show the image as output

# second level of gaussian smoothing
level_2 = ndimage.gaussian_filter(brain_image, sigma=10)
plt.imshow(level_2)

plt.imshow(level_2, cmap='Greys_r')     # use the reverse greyscale colormap
plt.show()

plt.hist(level_2, bins=10)              # plot the histogram   
plt.show()       # show the image as output

# third level of gaussian smoothing
level_3 = ndimage.gaussian_filter(brain_image, sigma=20)
plt.imshow(level_3)

plt.imshow(level_3, cmap='Greys_r')    # use the reverse greyscale colormap
plt.show()

plt.hist(level_3, bins=10)             # plot the histogram   
plt.show()        # show the image as output

# fourth level of gaussian smoothing
level_4 = ndimage.gaussian_filter(brain_image, sigma=30)
plt.imshow(level_4)

plt.imshow(level_4, cmap='Greys_r')    # use the reverse greyscale colormap
plt.show()

plt.hist(level_4, bins=10)             # plot the histogram   
plt.show()        # show the image as output

# fifth level of gaussian smoothing
level_5 = ndimage.gaussian_filter(brain_image, sigma=40)
plt.imshow(level_5)

plt.imshow(level_5, cmap='Greys_r')     # use the reverse greyscale colormap
plt.show()

plt.hist(level_5, bins=10)             # plot the histogram   
plt.show()        # show the image as output

# sixth level of gaussian smoothing 
level_6 = ndimage.gaussian_filter(brain_image, sigma=50)
plt.imshow(level_6)

plt.imshow(level_6, cmap='Greys_r')    # use the reverse greyscale colormap
plt.show()

plt.hist(level_6, bins=10)             # plot the histogram   
plt.show()        # show the image as output
