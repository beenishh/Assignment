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
plt.show()
