# Importing libraries
import reading_benchmark  as rb
import cv2 as cv
import utils as ut
import os
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


# colors 
# grey scale: 0 , 229 , 99 -> black , grey , grey (obstacle)

def Astar(img_path,start,end):
    image=cv.imread(img_path,0)
    rows,cols=(1073,1073)    
    # image (grey scale) to a matrix of 0 and 1 
    for i in range(rows):
        for j in range(cols):
            if image[i,j] == 0 or image[i,j] == 99: 
                image[i,j] = 0 #obstacle
            elif image[i,j] == 229:
                image[i,j] = 1
    
    grid = Grid(matrix=image)
    start = grid.node(start[0],start[1])
    end = grid.node(end[0],end[1])
    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    path, runs = finder.find_path(start, end, grid)

    #Saving results in file
    file_path = '/home/aisha/PFE/implementations/UAV-Path-Planning/src/tests/output/'
    with open(os.path.join(file_path , 'myfile.txt'),"w") as file:
        matrix_path=grid.grid_str(path=path, start=start, end=end)
        file.write(matrix_path)
            
    #Draw path in the image and save it
    image=cv.imread(img_path)
    new_image = ut.draw_path(image,path)
    saving_path = '/home/aisha/PFE/implementations/UAV-Path-Planning/src/tests/output/'
    cv.imwrite(os.path.join(saving_path , 'new_image.png'), new_image)


#TEST 
img_path = "/home/aisha/PFE/implementations/UAV-Path-Planning/data/room-png/64room_000.png"
start = (10, 200)
end = (90, 1009)
Astar(img_path,start,end)
