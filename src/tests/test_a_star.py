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

start = (133, 30)
end = (21, 201)

easy_output=[]
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
                easy_output.append(room_path.room_path("new_"+str(image),"astar","easy" , path,length,runs,time.time() - start_time))
            else:
                print(str(image) ,"invalid end")
        else:
            print(str(image),"invalid start")
    else:
        print("image is None")
file.write("\nEASY TEST \n")
print("length (easy output) : ",len(easy_output))        
for i in range(len(easy_output)):
    pathInfo = easy_output[i].path_info()
    print(pathInfo)
    file.write((str(pathInfo)+"\n"))


#-------------------Medium TEST---------------------------------------- 

# CHANGE START , END

start = (18, 30)
end = (21, 1001)

medium_output=[]
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
                medium_output.append(room_path.room_path("new_"+str(image),"astar","medium" , path,length,runs,time.time() - start_time))
                
            else:
                print(str(image) ,"invalid end")
        else:
            print(str(image),"invalid start")
    else:
        print("image is None")

file.write("\nMEDIUM TEST \n")
print("length (medium output) : ",len(medium_output))        
for i in range(len(medium_output)):
    pathInfo = medium_output[i].path_info()
    print(pathInfo)
    file.write((pathInfo+"\n"))


#-------------------HARD TEST---------------------------------------- 

# CHANGE START , END

start = (12, 30)
end = (1040, 990)

hard_output=[]
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
                hard_output.append(room_path.room_path("new_"+str(image),"astar","hard" ,path, length,runs,time.time() - start_time))
            else:
                print(str(image) ,"invalid end")
        else:
            print(str(image),"invalid start")
    else:
        print("image is None")
file.write("\nHARD TEST \n")
print("length (hard output) : ",len(hard_output))        
for i in range(len(hard_output)):
    pathInfo = hard_output[i].path_info()
    print(pathInfo)
    file.write((pathInfo+"\n"))

