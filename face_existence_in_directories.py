import cv2
import os
import pywt
import numpy as np
def extract(img):
                 blur = cv2.GaussianBlur(img,(5,5),0)
                 cA, cD =  pywt.dwt2(blur, 'haar') #Co-efficients returned
                 return cA

def load_images_from_folder(folder):  # function loading the program  from folder#
    images = []
    for filename in os.listdir(folder):   # opening the file from the folder#     
        img = cv2.imread(os.path.join(folder,filename)) #reading the image from the folder and file#
        if img is not None:
            images.append(img)     #updating the images#
    return images

def euc_dist( tst, db):    #finds euclidian distance between the two images
                       return np.sum((tst-db)**2)   # returns the sum value( x1-x2) square

N=list(range(40)) #it generates a list of numbers, which is generally used to iterate over with 'for' loops from 0 to (n-1)
im2=list(range(10))

E=load_images_from_folder("E:/Python/face/orl_faces/new_face")  #E= reading the folder#
for n in range(10):  # n is variable#
    im2[n]= extract(E[n]) # jumps to function 'extract' takes only LL#
img=cv2.imread("E:/Python/face/orl_faces/new_face/test.jpg")# reads the test images#
cv2.imshow('Test Image',img)
tst = extract(img)  # jumps to the function extract and collects cA

k=0                    
for r in range(10):
       E4=euc_dist(im2[r],tst) # jumps t0 function euclidian
       N[k]=E4   # stores it in E4#
       k+=1      
large1=max(N)    # large = maxm value of N#
for u in range(10):
        N[u]=N[u]/large1  # rounds of the value#
for z in range(10):
    cv2.imshow('data'+str(z),E[z])
if N[u]<=0.55:
          print('Match found')
          data_index=np.argmin(N)
          for z in range(5):
              cv2.imshow('Matched Image',E[data_index]) # Thresholding#
elif N[u]>0.55:
          print('Match not found') 
cv2.waitKey(0)
cv2.destroyAllWindows()