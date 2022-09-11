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
file= open("/home/aisha/PFE/implementations/UAV-Path-Planning/src/tests/output/output_a_star/recap.txt","w")
#-------------------EASY TEST---------------------------------------- 

file.write("\nEASY TEST \n")

start = (133, 30)
end = (21, 201)

for image in listdir(folder_dir):
    img_path=folder_dir+"/"+str(image)
    img=cv.imread(img_path,0)
    if img is not None:
        if ut.isValid(img_path,start):
            if ut.isValid(img_path,end):
                #print(str(image))
                start_time = time.time()
                path, runs , length = Astar(img_path,start,end,"new_"+str(image),"easy")
                #print("--- %s seconds ---" % (time.time() - start_time))
                pathInfo=(room_path.room_path("new_"+str(image),"astar","easy" , path,length,runs,time.time() - start_time)).path_info()
                file.write(pathInfo+"\n")
                
            else:
                print(str(image) ,"invalid end")
        else:
            print(str(image),"invalid start")
    else:
        print("image is None")
    


#-------------------Medium TEST---------------------------------------- 
file.write("\nMEDIUM TEST \n")

# CHANGE START , END

start = (18, 30)
end = (21, 1001)


for image in listdir(folder_dir):
    img_path=folder_dir+"/"+str(image)
    img=cv.imread(img_path,0)
    if img is not None:
        if ut.isValid(img_path,start):
            if ut.isValid(img_path,end):
                #print(str(image))
                start_time = time.time()
                path, runs , length = Astar(img_path,start,end,"new_"+str(image),"medium")
                #print("--- %s seconds ---" % (time.time() - start_time))
                pathInfo=(room_path.room_path("new_"+str(image),"astar","medium" , path,length,runs,time.time() - start_time)).path_info()
                file.write(pathInfo+"/n")
            else:
                print(str(image) ,"invalid end")
        else:
            print(str(image),"invalid start")
    else:
        print("image is None")



#-------------------HARD TEST---------------------------------------- 

file.write("\nHARD TEST \n")

# CHANGE START , END

start = (12, 30)
end = (1040, 990)


for image in listdir(folder_dir):
    img_path=folder_dir+"/"+str(image)
    img=cv.imread(img_path,0)
    if img is not None:
        if ut.isValid(img_path,start):
            if ut.isValid(img_path,end):
                #print(str(image))
                start_time = time.time()
                path, runs , length = Astar(img_path,start,end,"new_"+str(image),"hard")
                #print("--- %s seconds ---" % (time.time() - start_time))
                pathInfo = (room_path.room_path("new_"+str(image),"astar","hard" ,path, length,runs,time.time() - start_time)).path_info()
                file.write(pathInfo+"/n")
            else:
                print(str(image) ,"invalid end")
        else:
            print(str(image),"invalid start")
    else:
        print("image is None")


