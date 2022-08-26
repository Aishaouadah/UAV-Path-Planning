# for each image in benchmark find path for the given start and end (save images with path) 
# for each image save time needed to look for the path
from ..uav_path_planning import uav_path_planning_a_star as pp

#TEST 
img_path = "/home/aisha/PFE/implementations/UAV-Path-planning/data/room-png/64room_000.png"
start = (10, 200)
end = (90, 1009)
pp.Astar(img_path,start,end)
