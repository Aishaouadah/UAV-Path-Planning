"""
Reading MovingAI benchmarks (2D Grid Benchmark)
file format: image (png)
[Source](https://movingai.com/benchmarks/room/index.html) 
About images: 
    each pixel has the color of:
    # [229 229 229] Grey  -> not occupied cell
    # [0   0   0] Black   -> occupied cell (obstacle)
    # [0 127 0]Green      -> occupied cell (obstacle)
"""

# IMPORTS 
import sys
import cv2 as cv
import os
import numpy as np

# Checking colors 
image = cv.imread('/home/aisha/PFE/implementations/UAV-Path-planning/data/room-png/16room_002.png')
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