import networkx as nx
import matplotlib.pyplot as plt
import cv2 as cv

def draw_graph():
    pass


def show_image(image):
    
    print(image.shape)
    if image is None:
        print("image vide")
    else:
        cv.imshow('image', image) 
        cv.waitKey(0)
        cv.destroyAllWindows()
#TEST
#show_image(image)


# COLORING PIXELS 

def coloring_pixel(img_path,color):
    img = cv.imread(img_path)
    if img is None:
        print("None")
    else:     
        for i in range(30):
            for j in range(30):
                img[i,j] = color
        show_image(img)

#TEST 
'''
color = [255, 0, 0]
img_path = "/home/aisha/PFE/implementations/UAV-Path-planning/data/room-png/8room_000.png"
coloring_pixel(img_path,color)
'''