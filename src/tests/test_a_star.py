""" 
for each image in benchmark find path for the given start and end (save images with path) 
for each image save time needed to look for the path
"""
from os import listdir
import cv2 as cv
from src.uav_path_planning.uav_path_planning_a_star import Astar
from src.uav_path_planning import utils as ut



folder_dir = "/home/aisha/PFE/implementations/UAV-Path-Planning/data/room-png"

#-------------------EASY TEST---------------------------------------- 

start = (7, 25)
end = (19, 19)


for image in listdir(folder_dir):
    img_path=folder_dir+"/"+str(image)
    img=cv.imread(img_path,0)
    if img is not None:
        if ut.isValid(start,img):
            if ut.isValid(end,img):
                print(str(image))
                Astar(img_path,start,end,"new_"+str(image))
            else:
                print("invalid end")
        else:
            print("invalid start")
    else:
        print("image is None")

#-------------------Medium TEST---------------------------------------- 

# CHANGE START , END


#-------------------HARD TEST---------------------------------------- 

# CHANGE START , END