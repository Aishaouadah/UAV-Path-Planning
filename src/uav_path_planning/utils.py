import math
import numpy as np
import cv2 as cv



def image_none(img_path):
    image=cv.imread(img_path)
    return image


def show_image(image):
    cv.imshow('image', image) 
    cv.waitKey(0)
    cv.destroyAllWindows()

#TEST
#img_path = "/home/aisha/PFE/implementations/UAV-Path-planning/data/room-png/8room_000.png"
#image=image_none(img_path)
#if image is not None:
#    show_image(image)


'''Fitness function: function that evaluate a solution
    the Fitness function is the path length  '''
    #soltuion = "014523"
    #fitness = length(0,1)+length(1,4)+length(4,5)+length(5,2)+length(2,3)

def euclidean_distance(node1, node2):
    return math.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)

def manhattan_distance(node1, node2):
    return abs(node1.x - node2.x) + abs(node1.y - node2.y)
  
# COLORING PIXELS 

def coloring_pixel(image,color,pixel):
    if image is  not None:
        image[pixel[0],pixel[1]]=color
        return image
        
#TEST 
#color = [255, 0, 0]
#pixel=[0,2] 
#img_path = "/home/aisha/PFE/implementations/UAV-Path-planning/data/room-png/8room_000.png"
# coloring_pixel(img_path,color,pixel)

# define start and goal != of black and green (old color == white)
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

#TEST 

#start = [123, 12]
#goal = [125, 122]
#img_path = "/home/aisha/PFE/implementations/UAV-Path-planning/data/room-png/8room_000.png"
# image = image_none(img_path)
# print(image[start[0],start[1]])
# print(image[goal[0],goal[1]])
# show_image(define_start_goal(image,start,goal))


def draw_path(image_path,matrix_path):
    image=image_none(image_path)
    rows , cols = (1073 , 1073)
    if image is not None:
        new_image = image
        #get path reading the file
        for i in range(rows):
            for j in range(cols):
                if matrix_path[i][j] == 'x':
                    new_image[i][j] = 11 #yellow 
    return new_image

