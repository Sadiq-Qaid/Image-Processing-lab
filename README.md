# 1) Develop a program to display grayscale image using read and write operations

 # Description:
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
 # Description:
   When we are programming with OpenCV in Python, we often need images with specific dimensions. For example, let’s suppose that we want to resize a large image to fit on our computer screen and we need to shrink it. So, how we can do that?

We already learned that a digital image is presented in our computer by a matrix of pixels and each pixel has a specific value. So, if we want to resize our image, we just need to multiply values of our pixels with some scalar. In order to do that we just need to define coordinates of our resized image and apply function cv2.resize(). So, let’s see how it works:
 # Code
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

# Description:
 When we perform rotation in linear algebra we always rotate along the center of the coordinate system, However, in OpenCV while processing images we can also rotate our image along arbitrary point which can be defined as an additional parameter of our function. For instance, very often this parameter can be a center of the image and it will be defined in the following way.
 After defining a rotation matrix M we need to call cv2.getRotationMatrix2D() function which has few arguments. The first argument is the point around which we want to rotate the image, in our case it will be the center.
 Finally, we can apply the rotation to our image using cv2.warpAffine()method. We need to specify our rotation matrix M and the height and the width of our output image.
 
# Code
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
# Description:
In digital image processing, the sum of absolute differences (SAD) is a measure of the similarity between image blocks. It is calculated by taking the absolute difference between each pixel in the original block and the corresponding pixel in the block being used for comparison

Mean is most basic of all statistical measure. Means are often used in geometry and analysis; a wide range of means have been developed for these purposes. In contest of image processing filtering using mean is classified as spatial filtering and used for noise reduction.
# Code
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
# white) colour.
# Description:
Binary images are images whose pixels have only two possible intensity values. Numerically, the two values are often 0 for black, and either 1 or 255 for white. The main reason binary images are particularly useful in the field of Image Processing is because they allow easy separation of an object from the background.

In digital photography, computer-generated imagery, and colorimetry, a grayscale or image is one in which the value of each pixel is a single sample representing only an amount of light; that is, it carries only intensity information. Grayscale images, a kind of black-and-white or gray monochrome, are composed exclusively of shades of gray.
# Code

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
# colour spaces.
# Description:
Color spaces are different types of color modes, used in image processing and signals and system for various purposes. The color spaces in image processing aim to facilitate the specifications of colors in some standard way. Different types of color spaces are used in multiple fields like in hardware, in multiple applications of creating animation, etc.
# Code 
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
# Description:
For a two-dimensional array, in order to reference every element, we must use two nested loops. This gives us a counter variable for every column and every row in the matrix. int cols = 10; int rows = 10; int [] [] myArray = new int [cols] [rows]; // Two nested loops allow us to visit every spot in a 2D array Creating Arrays. You can create an array by using the new operator with the following syntax − Syntax arrayRefVar = new dataType[arraySize]; The above statement does two things − It creates an array using new dataType[arraySize]. It assigns the reference of the newly created array to the variable arrayRefVar.
# Code

import numpy

from PIL import Image

imarray = numpy.random.rand(512,1024,3) * 255

imarray[0:512,0:1024] = [100,0,255]

im = Image.fromarray(imarray,&#39;RGB&#39;)

im.save(&#39;result_image.png&#39;)

im.show()


# Output: 
![image](https://user-images.githubusercontent.com/72402606/104433780-7d510980-55b0-11eb-8ee4-cbf70bd161d9.png)
