import os
import numpy as np
import cv2

img = np.zeros((500, 512, 3))

file = open('/Users/richardfeng/Desktop/221202_153132.fft', 'rb')

dataSize = os.path.getsize('/Users/richardfeng/Desktop/221202_153132.fft')
frameNumber = int(dataSize/(500*1024))

file.seek(1024, os.SEEK_SET)
fftData = file.read();
count = 0;

for frame in range(0, frameNumber):
    
    title = 'FFT frame'
    polar = 'FFT frame'
    
    for line in range(0, 500):
        for freq in range(0, 512):
            
            value = fftData[count]/512
            img[line, freq, 0] = value # B
            img[line, freq, 1] = value # G
            img[line, freq, 2] = value # R
            count = count + 2
            
    cv2.imshow(title, img)
    cv2.imshow(polar, img)
    
    key = cv2.waitKey(5)
    
    if (key == 27):
        break
        
cv2.destroyAllWindows()
    