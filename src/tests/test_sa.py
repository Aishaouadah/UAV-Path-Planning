""" 
for each image, in benchmark find path for the given start and end (save images with path) 
for each image, save time needed to look for the path
"""
from os import listdir
import time
import cv2 as cv
from src.uav_path_planning.uav_path_planning_sa import SA
from src.uav_path_planning import room_path 
from src.uav_path_planning import utils as ut


folder_dir = "/home/aisha/PFE/implementations/UAV-Path-Planning/data/room-png"
file = open("/home/aisha/PFE/implementations/UAV-Path-Planning/src/tests/output/output_sa/all_results.txt","w")


#-------------------PARAMETER TUNING---------------------------------------- 

file.write("\nPARAMETER TUNING \n")

IT = [ 2 ] 
FT = [ 0 ]
N =[ 2 ] 
NT = [ 2] 
alpha = [ 0.8 ]
images=["8room_001.png" ] #32 #,"16room_000.png","32room_000.png","64room_000.png"] # 128

start = (50, 30)
end = (21, 10)

easy_output =[]
i=0

for image in images:
    parameters = {}
    for it in IT:
        parameters['IT'] = it     # Initial temperature
        for ft in FT:
            parameters['FT'] = ft     # Final temperature 
            for n in N:
                parameters['N']  = n      # Number of iterations
                for nt in NT:
                    parameters['NT']= nt       # Number of iterations per Temperature 
                    for a in alpha:
                        parameters['alpha'] = a  # Geometric Coefficient alpha
                        img_path=folder_dir+"/"+str(image)
                        img=cv.imread(img_path,0)
                        if img is not None:
                            if ut.isValid(img_path,start):
                                if ut.isValid(img_path,end):
                                    print(str(image))
                                    start_time = time.time()
                                    path , length = SA(img_path,start,end,str(i)+"new_"+str(image),parameters,"easy")
                                    print("path = ", path)
                                    print("--- %s seconds ---" % (time.time() - start_time))
                                    easy_output.append(room_path.room_path(str(i)+"new_"+str(image),"SA","easy" ,path, length,0,time.time() - start_time))                                     
                                    pathInfo = easy_output[-1].path_info()
                                    print(pathInfo)
                                    temp= str(pathInfo) +"it: "+str(it)+" ft: "+str(ft)+" n: "+str(n)+" nt: "+str(nt)+" alpha: "+str(a) + "\n"
                                    print(temp)
                                    file.write(temp)
                                    i=i+1
                                else:
                                    print(str(image) ,"invalid end")
                            else:
                                print(str(image),"invalid start")
                        else:
                            print("image is None")
"""
parameters={'IT':1,'FT':1,'N':1,'NT':1,'alpha':0.9}

#-------------------EASY TEST---------------------------------------- 

start = (133, 30)
end = (21, 201)

easy_output=[]
for image in listdir(folder_dir):
    img_path=folder_dir+"/"+str(image)
    img=cv.imread(img_path,0)
    if img is not None:
        if ut.isValid(img_path,start):
            if ut.isValid(img_path,end):
                #print(str(image))
                start_time = time.time()
                path , length = SA(img_path,start,end,"new_"+str(image),parameters,"easy")
                #print("--- %s seconds ---" % (time.time() - start_time))
                easy_output.append(room_path.room_path("new_"+str(image),"SA","easy",path,0 , length,time.time() - start_time))
            else:
                print(str(image) ,"invalid end")
        else:
            print(str(image),"invalid start")
    else:
        print("image is None")


file.write("\nEASY TEST \n")
print("length (medium output) : ",len(easy_output))        
for i in range(len(easy_output)):
    pathInfo = easy_output[i].path_info()
    print(pathInfo)
    file.write((pathInfo+"\n"))


#-------------------Medium TEST---------------------------------------- 

start = (18, 30)
end = (21, 1001)

medium_output=[]
for image in listdir(folder_dir):
    img_path=folder_dir+"/"+str(image)
    img=cv.imread(img_path,0)
    if img is not None:
        if ut.isValid(img_path,start):
            if ut.isValid(img_path,end):
                #print(str(image))
                start_time = time.time()
                path , length = SA(img_path,start,end,"new_"+str(image),parameters,"medium")
                #print("--- %s seconds ---" % (time.time() - start_time))
                medium_output.append(room_path.room_path("new_"+str(image),"SA","medium",path,0 , length,time.time() - start_time))
            else:
                print(str(image) ,"invalid end")
        else:
            print(str(image),"invalid start")
    else:
        print("image is None")

# CHANGE START , END

file.write("\nMEDIUM TEST \n")
print("length (medium output) : ",len(medium_output))        
for i in range(len(medium_output)):
    pathInfo = medium_output[i].path_info()
    print(pathInfo)
    file.write((pathInfo+"\n"))


#-------------------HARD TEST---------------------------------------- 


start = (12, 30)
end = (1040, 990)

hard_output=[]
for image in listdir(folder_dir):
    img_path=folder_dir+"/"+str(image)
    img=cv.imread(img_path,0)
    if img is not None:
        if ut.isValid(img_path,start):
            if ut.isValid(img_path,end):
                #print(str(image))
                start_time = time.time()
                path , length = SA(img_path,start,end,"new_"+str(image),parameters,"hard")
                #print("--- %s seconds ---" % (time.time() - start_time))
                hard_output.append(room_path.room_path("new_"+str(image),"SA","hard",path ,0, length,time.time() - start_time))
            else:
                print(str(image) ,"invalid end")
        else:
            print(str(image),"invalid start")
    else:
        print("image is None")

file.write("\nHARD TEST \n")
print("length (hard output) : ",len(hard_output))        
for i in range(len(hard_output)):
    pathInfo = hard_output[i].path_info()
    print(pathInfo)
    file.write((pathInfo+"\n"))

"""