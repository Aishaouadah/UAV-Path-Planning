#NOTE 
""" 
SA Algorithm: 
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

"""parameter setting can have a significant impact on the SA's performance."""

# Imports 
import math
import random as rd 
import src.uav_path_planning.utils as ut
import cv2 as cv
import os


def findNeighbors(matrix,node):
    #check validity and return neighbors to choose randomly one of them
    neighbors=[]
    if matrix[node[0]+1,node[1]] == 1:
        neighbors.append((node[0]+1,node[1]))
    if matrix[node[0],node[1]+1]==1:
        neighbors.append((node[0],node[1]+1))

    if matrix[node[0]+1,node[1]+1]==1:
        neighbors.append((node[0]+1,node[1]+1))

    if matrix[node[0]-1,node[1]]==1:
        neighbors.append((node[0]-1,node[1]))
        
    if matrix[node[0],node[1]-1]==1:
        neighbors.append( (node[0],node[1]-1))

    if matrix[node[0]-1,node[1]-1]==1:
        neighbors.append((node[0]-1,node[1]-1))

    if matrix[node[0]-1,node[1]+1]==1:
        neighbors.append((node[0]-1,node[1]+1))

    if matrix[node[0]+1,node[1]-1]==1:
        neighbors.append((node[0]+1,node[1]-1)) 

    return neighbors

def generatePath(matrix,start,end): 
    path=[]
    path.append(start)
    node=start 
    while(node!=end):
        neighbors = findNeighbors(matrix,node)
        node=neighbors[rd.randint(0,len(neighbors)-2)]
        path.append(node)
    return path

def generateNeighboringPath(matrix,path): 
    x=rd.randint(0,len(path)-2)
    neighbors=findNeighbors(matrix,path[x])
    output=path.copy()
    output[x]=neighbors[rd.randint(0,len(neighbors)-2)] 
    output[x+1:]=generatePath(matrix,output[x+1],output[-1])
    return output

def cost(path):
    distance=0
    for i in range(len(path)-1):
        distance+=ut.octile_distance(path[i],path[i+1])
    return distance

def sa(matrix,start,end , parameters):  
    CT = parameters['IT']  # Current temperature
    N= parameters['N']
    NT= parameters['NT'] 
    alpha = parameters['alpha']
    FT = parameters['FT']
    CP = generatePath(matrix,start,end) # current path (random)
    CL = cost(CP) 
    OP = CP # optimal path
    OL = CL
    for i in range(N):
        print("i= ",i)
        for j in range(NT):
            RP = generateNeighboringPath(matrix,CP)
            RL = cost(RP)  
            if RL < CL:
                CP = RP
                CL = RL 
            else: 
                p = math.exp(-(RL-CL)/CT) # Transition Probability 
                r= rd.uniform(0, 1)
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


# Save image
def SA(img_path,start,end,image_name,parameters,test):
    image=ut.imageToMatrix(img_path)
    op , ol = sa(image,start,end,parameters) 
    #Draw path in the image and save it
    image=cv.imread(img_path)
    new_image = ut.draw_path(img_path,op) 
    saving_path = '/home/aisha/PFE/implementations/UAV-Path-Planning/src/tests/output/output_sa/'+test
    cv.imwrite(os.path.join(saving_path ,image_name), new_image)
    return op, ol 
