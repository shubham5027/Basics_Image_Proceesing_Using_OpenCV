import cv2
import numpy as np


#Reading the image  (numpy array
# img=cv2.imread('dd973ac116a977c8dd5296b0da504b8c.jpg')
# img2=cv2.imread('depositphotos_3191160-stock-photo-blurry-bright-background.jpg')
# print(img)
#
#
# #Showing the image
# cv2.imshow('window',img)
# cv2.imshow('window',img2)
# cv2.waitKey(0)


#RGB to Grayscale

# img3=cv2.imread('dd973ac116a977c8dd5296b0da504b8c.jpg')
# # cv2.imshow('window',img3)
# # cv2.waitKey(0)
#
# img_gray=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
# cv2.imshow('window',img_gray)
# cv2.waitKey(0)

#Separating RGB channels
# img3=cv2.imread('Safeimagekit-resized-img.jpg')
#
# img_red=img3[:,:,2]
# img_green=img3[:,:,1]
# img_blue=img3[:,:,0]
#
# img=np.hstack((img_red,img_green,img_blue))
# cv2.imshow('window',img)
# cv2.waitKey(0)


#Resizing images

# img3=cv2.imread('dd973ac116a977c8dd5296b0da504b8c.jpg')
# re_size=cv2.resize(img3,(400,400))
# cv2.imshow('window',re_size)
# cv2.waitKey(0)

#flipping images
# img3=cv2.imread('Safeimagekit-resized-img.jpg')
# flip_img=cv2.flip(img3,-1)
# cv2.imshow('window',flip_img)
# cv2.waitKey(0)

# img3=cv2.imread('Safeimagekit-resized-img.jpg')
# flip_img=cv2.flip(img3,0)
# cv2.imshow('window',flip_img)
# cv2.waitKey(0)


#cropping the image

# img3=cv2.imread('Safeimagekit-resized-img.jpg')
# img_crop=img3[100:300,100:200]
# cv2.imshow('window',img_crop)
# cv2.waitKey(0)

#saving the images

# img3=cv2.imread('Safeimagekit-resized-img.jpg')
# img_crop=img3[100:300,100:200]
# cv2.imwrite('krishna.jpg',img_crop)
# cv2.waitKey(0)

#Drawing shapes and text on top of image

# img3=cv2.imread('dd973ac116a977c8dd5296b0da504b8c.jpg')
#
# cv2.rectangle(img3,pt1=(300,300),pt2=(550,700),color=(255,0,255),thickness=5)
# cv2.circle(img3,center=(400,300),radius=150,color=(255,0,0),thickness=5)
# cv2.line(img3,pt1=(400,300),pt2=(6000,700),color=(255,255,255),thickness=5)
# cv2.putText(img3,org=(40,60),fontScale=2,color=(0,255,255),thickness=3,lineType=cv2.LINE_8,text='JAY SHREE RAM',fontFace=cv2.FONT_HERSHEY_TRIPLEX)
#
#
# cv2.imshow('window',img3)
# cv2.waitKey(0)


#Images Events
# def draw(events,x,y,flags,params):
#     print("triggered")
#
# cv2.namedWindow(winname='window')
# cv2.setMouseCallback('window',draw)
#
#
# img3=cv2.imread('Safeimagekit-resized-img.jpg')
# while True :
#     cv2.imshow('window',img3)
#     if cv2.waitKey(1) & 0xff ==ord('5'):
#      break
# cv2.destroyWindow()


# def draw(event, x, y, flags, params):
#     if event==4:
#         print("hello")
#     elif event==1:
#         print("good")
#     else:
#         print("AA")
#
# cv2.namedWindow(winname='window')
# cv2.setMouseCallback('window', draw)
#
#
# img3 = cv2.imread('Safeimagekit-resized-img.jpg')
# while True:
#     cv2.imshow('window', img3)
#     if cv2.waitKey(1) & 0xff == ord('5'):
#         break
# cv2.destroyWindow()

#Working Vidios using OpenCv


# cap=cv2.VideoCapture(0)
# fourcc =cv2.VideoWriter_fourcc(*'XVID')
# out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
#
# while True:
#     ret, frame =cap.read()
#     out.write(frame)
#
#     cv2.imshow("webcam",frame)
#     if cv2.waitKey(1) & 0xff == ord('5'):
#         break
# out.release()
# cv2.destroyWindow()



