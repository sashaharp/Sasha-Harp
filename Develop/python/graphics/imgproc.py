import numpy as np
import matplotlib.pyplot as plt

imageSource = plt.imread("test0.jpg")
imageArray = imageSource[:, :, :]
imageArray.setflags(write=1)

print(imageArray[20][20])

chunk = imageArray[10:10+10, 10:10+10, :]
print(chunk)

for i in range(imageArray.shape[0]//10):
    for j in range(imageArray.shape[1]//10):
        chunk = imageArray[i*10:i*10+10, j*10:j*10+10, :]
        g = np.sum(chunk[:,:,1])/np.sum(chunk.flatten)
        
        """g = imageArray[i][j][1]/(imageArray[i][j][0] + imageArray[i][j][1] + imageArray[i][j][2])
        if g>0.365:
            imageArray[i,j,:] = [255, 255, 255] 
        if g<=0.369 and g >= 0.328:
            imageArray[i, j, :] = [0, 0, 0]"""

plt.axis("off")
plt.imshow(imageArray)
plt.show()