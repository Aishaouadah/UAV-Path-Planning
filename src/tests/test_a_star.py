""" 
for each image in benchmark find path for the given start and end (save images with path) 
for each image save time needed to look for the path
"""
from os import listdir
import time
import cv2 as cv
from src.uav_path_planning.uav_path_planning_a_star import Astar
from src.uav_path_planning import room_path 
from src.uav_path_planning import utils as ut


folder_dir = "/home/aisha/PFE/implementations/UAV-Path-Planning/data/room-png"

#-------------------EASY TEST---------------------------------------- 

start = (133, 30)
end = (21, 201)

easy_output=[]
for image in listdir(folder_dir):
    img_path=folder_dir+"/"+str(image)
    img=cv.imread(img_path,0)
    if img is not None:
        if ut.isValid(start,img):
            if ut.isValid(end,img):
                #print(str(image))
                start_time = time.time()
                path, runs , length = Astar(img_path,start,end,"new_"+str(image))
                #print("--- %s seconds ---" % (time.time() - start_time))
                easy_output.append(room_path.room_path("new_"+str(image),"astar","easy",path , length,runs,time.time() - start_time))
            else:
                print(str(image) ,"invalid end")
        else:
            print(str(image),"invalid start")
    else:
        print("image is None")

print("length (easy output) : ",len(easy_output))        
for i in range(len(easy_output)):
    easy_output[i].print_path()

#-------------------Medium TEST---------------------------------------- 

# CHANGE START , END


#-------------------HARD TEST---------------------------------------- 

# CHANGE START , END