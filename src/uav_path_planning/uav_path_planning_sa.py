#NOTE 
"""

Initialisation 
Trouver une solution initiale x ( aléatoirement ou avec une heuristique) 
Choisir in température initiale TO 
T=TO Température de Refroidissement 
Tant que Test d'arrêt non satisfait 
    Trouver x' solution voisine (x' £ N(x) ) 
    Calculer df= f(x') - f(x) 
    Choisir un bêta e [0,1],(un paramètre de tolérance) 
    Si df ,< 0 ou exp (—df) > beta (le critère de Metropolis) 
        Alors x = x' 
    Mettre a jour la température de refroidissement T (Abaisser In température) 
Fin boucle Tant que 

"""

"""In order to apply the SA algorithm to a specific problem, 
one must specify the neighbourhood structure and cooling schedule."""

"""These choices and their corresponding parameter
setting can have a significant impact on the SA's performance."""

# Imports 
import math
import numpy as np  
import random as rd 
import utils as ut
import cv2 as cv
import os

def findNeighbors(matrix,node):
    #check validity and return neighbors to choose randomly one of them
    neighbors=[]

    if matrix[node[0]+1,node[1]] == 1:
        neighbor = (node[0]+1,node[1])
        neighbors.append(neighbor)

    if matrix[node[0],node[1]+1]==1:
        neighbor = (node[0],node[1]+1)
        neighbors.append(neighbor)

    if matrix[node[0]+1,node[1]+1]==1:
        neighbor = (node[0]+1,node[1]+1)
        neighbors.append(neighbor)

    if matrix[node[0]-1,node[1]]==1:
        neighbor = (node[0]-1,node[1])
        neighbors.append(neighbor)
    
    if matrix[node[0],node[1]-1]==1:
        neighbor = (node[0],node[1]-1)
        neighbors.append(neighbor)

    if matrix[node[0]-1,node[1]-1]==1:
        neighbor = (node[0]-1,node[1]-1)
        neighbors.append(neighbor)

    if matrix[node[0]-1,node[1]+1]==1:
        neighbor = (node[0]-1,node[1]+1)
        neighbors.append(neighbor)

    if matrix[node[0]+1,node[1]-1]==1:
        neighbor = (node[0]+1,node[1]-1)
        neighbors.append(neighbor) 

    return neighbors


def generatePath(matrix,start,end):  #FIXME  are you sure about the generated path 😭 
    path=[]
    visited_nodes=[]
    path.append(start)
    node=start 
    while(node!=end):
        neighbors = findNeighbors(matrix,node)
        node=neighbors[rd.randint(0,len(neighbors)-1)]
        if node not in visited_nodes:
            visited_nodes.append(node) 
            path.append(node)
    return path

#TEST  

img_path = "/home/aisha/PFE/implementations/UAV-Path-Planning/data/room-png/64room_000.png"
matrix=ut.imageToMatrix(img_path)

#start=(10,10)
#end=(140,80)
#print(ut.isValid(img_path,start),ut.isValid(img_path,end))
#path=generatePath(matrix,start,end)
#image=ut.draw_path(img_path,path) 

#saving_path = '/home/aisha/PFE/implementations/UAV-Path-Planning/src/tests/output/output_sa'
#scv.imwrite(os.path.join(saving_path ,"new_64room_000.png"), image)
    

def generateNeighboringPath(matrix,path): 
    x=rd.randint(0,len(path)-2)
    print(x)
    neighbors=findNeighbors(matrix,path[x])
    output=path.copy()
    output[x]=neighbors[rd.randint(0,len(neighbors)-2)] 
    output[x+1:]=generatePath(matrix,output[x+1],output[-1])
    return output

#TEST
#path =[ (139, 75) ,(138, 76) , (138, 77) , (139, 76) , (140, 76) , (138, 75) ,(140, 77) ]
#print("path : " , path)
#new_path = generateNeighboringPath(matrix,path)
#print("new path : " ,new_path)


def cost(path):
    distance=0
    for i in range(len(path)-1):
        distance+=ut.euclidean_distance(path[i],path[i+1])
    return distance

#TEST

#print("path cost",cost (path)) 
#print("new path cost",cost (new_path)) 

# Initializing parameters

IT = 10   # Initial temperature
FT = 5   # Final temperature 
N= 10 # Number of iterations
NT= 5 # Number of iterations per Temperature 
alpha = 0.1
# Geometric Coefficient alpha
# Transition Probability p

def SA(matrix,start,end):  
    CT = IT   # Current temperature
    CP = generatePath(matrix,start,end) # current path (random)
    CL = cost(CP) 
    OP = CP # optimal path
    OL = CL
    for i in range(N):
        for j in range(NT):
            RP = generateNeighboringPath(matrix,CP)
            RL = cost(RP)
            if RL < CL:
                CP = RP
                CL = RL 
            else: 
                p = math.exp(-(RL-CL)/CT)
                r=rd.randint(0,1)
                if r<p:
                    CP = RP
                    CL = RL 
            if CL < OL:
                OP = CP
                OL = CL
        CT *= alpha 
        if CT <= FT:
            break 
    return OP , OL 


start=(10,10)
end=(14,40)
print(SA(matrix,start,end))
    
    