# 1) Develop a program to display grayscale image using read and write operations

 # Describtion
  Grayscaling is the process of converting an image from other color spaces e.g RGB, CMYK, HSV, etc. to shades of gray. It varies between complete black and complete white.

Importance of grayscaling –

Dimension reduction: For e.g. In RGB images there are three color channels and has three dimensions while grayscaled images are single dimensional.
Reduces model complexity: Consider training neural article on RGB images of 10x10x3 pixel.The input layer will have 300 input nodes. On the other hand, the same neural network will need only 100 input node for grayscaled images.
For other algorithms to work: There are many algorithms that are customized to work only on grayscaled images e.g. Canny edge detection function pre-implemented in OpenCV library works on Grayscaled images only.
# Code
import cv2
img= cv2.imread(&quot;app.jpg&quot;)
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite(&quot;opencv-greyscale.png&quot;,gray_image)
cv2.imshow(&quot;Gray_Scale&quot;,gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# output:
![image](https://user-images.githubusercontent.com/72402606/104429706-f00bb600-55ab-11eb-9f9c-47be74cb7566.png)


# 2) Develop a program to perform a linear transformation for an image
# (scaling &amp; rotation)
# a. Scaling:
import cv2 as c
import numpy as np
img= cv2.imread(&quot;app.jpg&quot;)
h,w=img.shape[0:2]
width=int(w*1)
hight=int(h*1)
dim =(width,hight)
res=c.resize(img,dim)
c.imshow(&quot;Scaling&quot;,res)
c.waitKey(0)
c.destroyAllWindows()

# Output:
![image](https://user-images.githubusercontent.com/72402606/104431462-eb480180-55ad-11eb-9a2a-19989d09936a.png)

# b. Rotation:
import cv2 as c
import numpy as np
img= cv2.imread(&quot;app.jpg&quot;)
h,w=img.shape[0:2]
rotationMatrix=cv2.getRotationMatrix2D((w/2,h/2),90,.5)
rotated_img=cv2.warpAffine(img,rotationMatrix,(w,h))
c.imshow(&quot;Orignal_Image&quot;,img)
c.imshow(&quot;rotation&quot;,rotated_img)
c.waitKey(0)
c.destroyAllWindows()

# Output:
![image](https://user-images.githubusercontent.com/72402606/104431835-5d204b00-55ae-11eb-8b4f-5539aa5ee0c0.png)

# 3)Develop a program to find sum and mean of a set of images

import cv2
import os
path=&#39;D:\images&#39;
imgs = []
files = os.listdir(path)
for file in files:
filepath=path+&quot;\\&quot;+file
imgs.append(cv2.imread(filepath))
i=0
im = []
for im in imgs:
#cv2.imshow(files[i], imgs[i])
im+=imgs[i]
i = i +1
cv2.imshow(&quot;Sum_OF_FOUR_IMAGES&quot;,im)
meanImg = im/len(files)
cv2.imshow(&quot;MEAN_OF_FOUR_IMAGES&quot;,meanImg)
cv2.waitKey(0)

# Output:

![image](https://user-images.githubusercontent.com/72402606/104432338-f0598080-55ae-11eb-96cb-4a2d47f4a533.png)

# 4)Develop a program to convert image into a binary (Black and
white) colour.
import cv2
img = cv2.imread(&#39;cat.jpg&#39;,2)
ret, bw_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow(&quot;Orignal_Image&quot;,img)
cv2.imshow(&quot;Binary Image&quot;,bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Output:
![image](https://user-images.githubusercontent.com/72402606/104432935-85f51000-55af-11eb-9dc9-979353ab15a7.png)

# 5)Develop a program to convert the given colour image to different
colour spaces.
import cv2
image = cv2.imread(&#39;cat.jpg&#39;)
img_HLS = cv2.cvtColor(image,cv2.COLOR_BGR2HLS)
img_HSV = cv2.cvtColor(image,cv2.cv2.COLOR_BGR2HSV)
img_RGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
cv2.imshow(&quot;original&quot;, image)
cv2.imshow(&quot;HLS&quot;, img_HLS)
cv2.imshow(&quot;HSV&quot;, img_HSV)
cv2.imshow(&quot;RGB&quot;, img_RGB)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Output:
![image](https://user-images.githubusercontent.com/72402606/104433325-fdc33a80-55af-11eb-80f8-c9b976511ff2.png)

# 6)Develop a program to create an image from 2D array (create an
# array of random size and density values).
import numpy
from PIL import Image
imarray = numpy.random.rand(512,1024,3) * 255
imarray[0:512,0:1024] = [100,0,255]
im = Image.fromarray(imarray,&#39;RGB&#39;)
im.save(&#39;result_image.png&#39;)
im.show()

# Output:
![image](https://user-images.githubusercontent.com/72402606/104433780-7d510980-55b0-11eb-8ee4-cbf70bd161d9.png)
