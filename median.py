import cv2
import numpy as np
from skimage import img_as_ubyte

## original image
img = cv2.imread('Lenna.png', 0)
img = img/img.max() 

x,y = img.shape
g = np.zeros((x,y), dtype=np.float32)
pepper = 0.1
salt = 0.95  
for i in range(x):
    for j in range(y):
        rdn = np.random.random()
        if rdn < pepper:
            g[i][j] = 0
        elif rdn > salt:
            g[i][j] = 1
        else:
            g[i][j] = img[i][j]

img_noise = g

# median filter
img_noise_median = np.clip(img_noise, -1, 1) #pixel value range
img_noise_median = img_as_ubyte(img_noise_median) #convert to uint8
denoise_median = cv2.medianBlur(img_noise_median, 5)

# preview the images
cv2.imshow('Original Image', img)
cv2.imshow('Image + Noise', img_noise)
cv2.imshow('noise Median', denoise_median)

cv2.waitKey(0)
cv2.destroyAllWindows()

# (optional) save the result
cv2.imwrite('noise median.jpg', img_as_ubyte(denoise_median))