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
file= open("/home/aisha/PFE/implementations/UAV-Path-Planning/src/tests/output/output_sa/all_results.txt","w")

#-------------------PARAMETER TUNING---------------------------------------- 
IT = [ 2,6,9]
FT = [ 1,2,3 ]
N =[ 5,8] 
NT = [ 5,8] 
alpha = [ 0.9 , 0.3 ]
images=["8room_000.png","16room_000.png","32room_000.png","64room_000.png"]

start = (133, 30)
end = (21, 201)
easy_output =[]

for it in IT:
    for ft in FT:
        for n in N:
            for nt in NT:
                for a in alpha:
                #test the 4 images and save results    
                    for image in images:
                       # Initializing parameters
                        parameters = {}
                        parameters['IT'] = it     # Initial temperature
                        parameters['FT'] = ft     # Final temperature 
                        parameters['N']  = n      # Number of iterations
                        parameters['NT']= nt       # Number of iterations per Temperature 
                        parameters['alpha'] = a  # Geometric Coefficient alpha

                        img_path=folder_dir+"/"+str(image)
                        img=cv.imread(img_path,0)
                        if img is not None:
                            if ut.isValid(img_path,start):
                                if ut.isValid(img_path,end):
                                    #print(str(image))
                                    start_time = time.time()
                                    print(img)
                                    path , length = SA(img_path,start,end,"new_"+str(image),parameters)
                                    #print("--- %s seconds ---" % (time.time() - start_time))
                                    easy_output.append(room_path.room_path("new_"+str(image),"SA","easy",path , length,time.time() - start_time))
                                else:
                                    print(str(image) ,"invalid end")
                            else:
                                print(str(image),"invalid start")
                        else:
                            print("image is None")


file.write("\nPARAMETER TUNING \n")
print("length (easy output) : ",len(easy_output))        
for i in range(len(easy_output)):
    pathInfo = easy_output[i].path_info()
    print(pathInfo)
    file.write((str(pathInfo)+"\n"))

#-------------------EASY TEST---------------------------------------- 
"""
start = (133, 30)
end = (21, 201)

easy_output=[]
for image in listdir(folder_dir):
    img_path=folder_dir+"/"+str(image)
    img=cv.imread(img_path,0)
    if img is not None:
        if ut.isValid(start,img):
            if ut.isValid(end,img):
                #print(str(image))
                start_time = time.time()
                path , length = SA(img_path,start,end,"new_"+str(image))
                #print("--- %s seconds ---" % (time.time() - start_time))
                easy_output.append(room_path.room_path("new_"+str(image),"SA","easy",path , length,time.time() - start_time))
            else:
                print(str(image) ,"invalid end")
        else:
            print(str(image),"invalid start")
    else:
        print("image is None")

print("length (easy output) : ",len(easy_output))        
for i in range(len(easy_output)):
    easy_output[i].print_path()

#-------------------Medium TEST---------------------------------------- 

# CHANGE START , END


#-------------------HARD TEST---------------------------------------- 

# CHANGE START , END


"""