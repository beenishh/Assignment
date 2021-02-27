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
