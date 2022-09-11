# Importing libraries
import cv2 as cv
import os
from src.uav_path_planning import utils as ut
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


# colors 
# grey scale: 0 , 229 , 99 -> black , grey , grey (obstacle)

def Astar(img_path,start,end,image_name,test):
    image=ut.imageToMatrix(img_path)
    grid = Grid(matrix=image)
    start = grid.node(start[0],start[1])
    end = grid.node(end[0],end[1])
    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    path, runs = finder.find_path(start, end, grid)
    print("path length: ",ut.octile(path) , "runs: " , runs)
        
    #Draw path in the image and save it
    image=cv.imread(img_path)
    new_image = ut.draw_path(img_path,path)
    saving_path = '/home/aisha/PFE/implementations/UAV-Path-Planning/src/tests/output/output_a_star/'+test
    cv.imwrite(os.path.join(saving_path ,image_name), new_image)
    
    return path, runs , ut.octile(path)

