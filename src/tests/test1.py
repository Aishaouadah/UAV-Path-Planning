""" 
for each image in benchmark find path for the given start and end (save images with path) 
for each image save time needed to look for the path
"""
from os import listdir
from src.uav_path_planning.uav_path_planning_a_star import Astar

#TEST 1
img_path = "/home/aisha/PFE/implementations/UAV-Path-Planning/data/room-png/64room_000.png"
start = (7, 25)
end = (19, 19)
#Astar(img_path,start,end)

# get the path/directory
folder_dir = "/home/aisha/PFE/implementations/UAV-Path-Planning/data/room-png"

for image in listdir(folder_dir):
    img_path=folder_dir+"/"+str(image)
    print(str(image))
    Astar(img_path,start,end,"new_"+str(image))