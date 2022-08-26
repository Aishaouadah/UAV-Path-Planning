import uav_path_planning.reading_benchmark   as rb
from uav_path_planning.uav_path_planning_a_star import Astar
#FIXME can't acess notebooks

#Run tests : call A* LAHC SA (40 image), generate comparative tables, plots (iterations) ... 


#TEST 
img_path = "/home/aisha/PFE/implementations/UAV-Path-Planning/data/room-png/64room_000.png"
start = (10, 200)
end = (90, 1009)
#images=rb.read_images("/home/aisha/PFE/implementations/UAV-Path-Planning/data/room-png")
Astar(img_path,start,end)