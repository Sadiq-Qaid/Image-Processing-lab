# 1) Develop a program to display grayscale image using read and write operations

import cv2
img= cv2.imread(&quot;app.jpg&quot;)
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite(&quot;opencv-greyscale.png&quot;,gray_image)
cv2.imshow(&quot;Gray_Scale&quot;,gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()




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



# 4)Develop a program to convert image into a binary (Black and
white) colour.
import cv2
img = cv2.imread(&#39;cat.jpg&#39;,2)
ret, bw_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow(&quot;Orignal_Image&quot;,img)
cv2.imshow(&quot;Binary Image&quot;,bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



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



# 6)Develop a program to create an image from 2D array (create an
# array of random size and density values).
import numpy
from PIL import Image
imarray = numpy.random.rand(512,1024,3) * 255
imarray[0:512,0:1024] = [100,0,255]
im = Image.fromarray(imarray,&#39;RGB&#39;)
im.save(&#39;result_image.png&#39;)
im.show()

# 7) a)Develop a program to find the neighbours of each element in the matrix.
  #  b)Write a program to find the sum of neighbour values in a matrix.

 

    import numpy as np
    axis = int(input("Enter the radius of the matrix: "))
    neighbor = int(input("Enter the 4 or 8 to calculate the neighbors: "))
    if neighbor == 4 or neighbor == 8:
    x =np.empty((axis,axis))
    y = np.empty((axis+2,axis+2))
    s =np.empty((axis,axis))
    
    # Generating the Values of the Matrix
    for i in range(0,axis):
        for j in range(0,axis):
            x[i][j]=int(i+j+1)
    # Printing the Values of the Generated Matrix
    print("Printing the Values of the Generated Matrix", end="\n")
    for i in range(0,axis):
        for j in range(0,axis):
            pass
            print(int(x[i][j]),end = '\t')
        print('\n')


    for i in range(0,axis+2):
        for j in range(0,axis+2):
            if i == 0 or i == axis+1 or j == 0 or j==axis+1:
                y[i][j]=0
            else:
                y[i][j]=x[i-1][j-1]
                
    # Printing the Values of the Matrix after padding with zeros
    print("The Values of the Matrix after padding with zeros:", end="\n")
    for i in range(0,axis+2):
        for j in range(0,axis+2):
            print(int(y[i][j]),end = '\t')
        print('\n')
    
    print("The neighbours of each element in the matrix:", end="\n")
    for i in range(0,axis):
        for j in range(0,axis):
            
            if neighbor == 4:                
                s[i][j]=((y[i][j+1]+y[i+1][j]+y[i+1][j+2]+y[i+2][j+1]))
                print(x[i][j],":",end = '\t')
                print(y[i][j+1],',',y[i+1][j],',',y[i+1][j+2],',',y[i+2][j+1])
                #print(s[i][j],end = '\t')
            elif neighbor ==8:
                    s[i][j]=((y[i][j]+y[i][j+1]+y[i][j+2]+y[i+1][j]+y[i+1][j+2]+y[i+2][j]+y[i+2][j+1]+y[i+2][j+2]))
                    print(x[i][j],":",end = '\t')
                    print(y[i][j],',',y[i][j+1],',',y[i][j+2],',',y[i+1][j],',',y[i+1][j+2],',',y[i+2][j],',',y[i+2][j+1],',',y[i+2][j+2])
                    #print(s[i][j],end = '\t')
        print('\n')
        
    print("The following matrix contains the sum of neighbour values in a matrix")
    for i in range(0,axis):
        for j in range(0,axis):
            
            if neighbor == 4:                
                s[i][j]=((y[i][j+1]+y[i+1][j]+y[i+1][j+2]+y[i+2][j+1]))
                print(s[i][j],end = '\t')
            elif neighbor ==8:
                s[i][j]=((y[i][j]+y[i][j+1]+y[i][j+2]+y[i+1][j]+y[i+1][j+2]+y[i+2][j]+y[i+2][j+1]+y[i+2][j+2]))
                print(s[i][j],end = '\t')
        print('\n')
else:
     print("Wrong neighbors, you have to select ether 4 or 8")
     
