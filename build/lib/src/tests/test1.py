""" 
for each image in benchmark find path for the given start and end (save images with path) 
for each image save time needed to look for the path
"""
#from src.uav_path_planning.uav_path_planning_a_star import Astar
#from src.uav_path_planning import uav_path_planning_a_star
from src.uav_path_planning import uav_path_planning_sa as sa

#TEST 1
img_path = "/home/aisha/PFE/implementations/UAV-Path-Planning/data/room-png/64room_000.png"
start = (10, 200)
end = (90, 1009)
#Astar(img_path,start,end)
sa.function()
