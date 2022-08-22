"""
Reading MovingAI benchmarks 
PNG,  2D Grid Benchmark
[Source](https://movingai.com/benchmarks/room/index.html) 

"""

# IMPORTS 
import sys
import cv2 as cv
import os
import numpy as np
import pyMetaheuristic

# Checking colors 
image = cv.imread('/home/aisha/PFE/implementations/UAV-Path-planning/data/room-png/16room_002.png')
# 1073*1073*3 == 277741 + 51662 + 3124584 -> True
#Matrix dim == 0 , 127 , 229 
# (only 3 colors) with this 3 combinaison 
unique , counts = np.unique(image, return_counts=True)
dict(zip(unique,counts))



#------------Reading all images---------------   
 
     
def read_images(folder):
    images=[]
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
            
    return images

#all images have same shape (1073,1073,3)  

#TEST
#images=read_images("/home/aisha/PFE/implementations/UAV-Path-planning/data/room-png")