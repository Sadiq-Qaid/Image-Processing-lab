#program to impelemnt negative image
import cv2 as c
import matplotlib.pyplot as plt
img = c.imread("lina.jpg",1)
color = ('b','g','r')
plt.imshow(img)
plt.show()
for i,col in enumerate(color):
    hist = c.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color =col)
    plt.xlim([0,256])
plt.show()

h,w = img.shape[0:2]
for i in range(0,h- 1):
    for j in range(0,w- 1):
        pixel = img[i][j]
        pixel[0] = 255 - pixel[0]
        pixel[1] = 255 - pixel[1]
        pixel[2] = 255 - pixel[2]
        img[i][j] = pixel

       
plt.imshow(img)
plt.show()
for i,col in enumerate(color):
    hist = c.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color =col)
    plt.xlim([0,256])
plt.show()
