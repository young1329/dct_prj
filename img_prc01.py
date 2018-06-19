'''
Image Filtering Compression
'''
import numpy as np
import matplotlib.pyplot as plt
import cv2
print cv2.__version__

N = 8

# read image file : 512x512
img01=cv2.imread('8vuLtqi.png',0)

#display image
#cv2.imshow('imge',img01)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

T = np.zeros((N,N));
for i in range(N):
    for j in range(N):
        if i==0:
            T[i,j]=1.0/np.sqrt(N)
        else:
            T[i,j]=np.sqrt(2./N) * np.cos(np.pi/N*(j+0.5)*i)

#define dummy variables
img = np.zeros((N,N))
img80=img
#two images after converting
DT = np.zeros((len(img01),len(img01[0])))
DT80=DT

Q80table=np.array([
    [6,4,4,6,10,16,20,24],
    [5,5,6,8,10,23,24,22],
    [6,5,6,10,16,23,28,22],
    [6,7,9,12,20,35,32,25],
    [7,9,15,22,27,44,41,31],
    [10,14,22,26,32,42,45,37],
    [20,26,31,35,41,48,48,40],
    [29,37,38,39,45,40,41,40]
])

Q50table = np.array([
    [16,11,10,16,24,40,51,61],
    [12,12,14,19,26,58,60,55],
    [14,13,16,24,40,57,69,56],
    [14,17,22,29,51,87,80,62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
])

for i in range(0,len(img01),N):
    for j in range(0,len(img01[0]),N):
        img = img01[i:i+N,j:j+N]
        img = img.astype(int)
        img = img -128
        img = np.dot(T,np.dot(img,T.T))
        img80 = np.round(img / Q80table)*Q80table
        img = np.round(img / Q50table)
        img = img*Q50table
        img80 = np.dot(T.T,np.dot(img80,T))+128
        img = np.dot(T.T,np.dot(img,T))
        img = img+128
        DT[i:i+N,j:j+N]=img
        DT80[i:i+N,j:j+N]=img80
    
DT=DT.astype(np.uint8)
DT80=DT80.astype(dtype='uint8')

cv2.imshow('org',img01)
cv2.imshow('Q50',DT)
cv2.imshow('Q80',DT80)
cv2.waitKey(0)
cv2.destroyAllWindows()
       