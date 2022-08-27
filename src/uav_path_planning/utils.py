import math
import numpy as np
import cv2 as cv
import os

def image_none(img_path):
    image=cv.imread(img_path)
    return image

def show_image(image):
    cv.imshow('image', image) 
    cv.waitKey(0)
    cv.destroyAllWindows()

def euclidean_distance(node1, node2):
    return math.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)

def manhattan_distance(node1, node2):
    return abs(node1.x - node2.x) + abs(node1.y - node2.y)
  
def coloring_pixel(image,color,pixel):
    if image is  not None:
        image[pixel[0],pixel[1]]=color
        return image

def define_start_goal(image,start,goal):
    start_color = [255, 0, 102] #pink 
    goal_color =  [0, 0, 204] #blue
    if image is not None:
        # should not be obstacle 
        if np.array_equal(image[start[0],start[1]],[229, 229, 229]) and np.array_equal(image[goal[0],goal[1]],[229, 229, 229]):
            image = coloring_pixel(image,start_color,start)
            image = coloring_pixel(image,goal_color,goal) 
            return image
        else: 
            print("Goal or Start is an obstacle, Redefine it!")
            return image

def draw_path(image,path):    
    if image is not None:
        for tuple in path:
            print(tuple)
            image[tuple[1],tuple[0]]=[0, 0, 255] #red
    return image

def save_image(img_path,path,image_name):
    image=cv.imread(img_path)
    new_image = draw_path(image,path)
    saving_path = '/home/aisha/PFE/implementations/UAV-Path-Planning/src/tests/output/'
    cv.imwrite(os.path.join(saving_path , image_name), new_image)    

def isValid(node,image):
    return  image[node[0],node[1]] == 299 