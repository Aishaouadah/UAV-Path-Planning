""" output structure: (room_name,method used, type de test, path, path length, operations, time)"""
class room_path:
    def __init__(self,room_name,method,test,path,path_length,operations,time):
        self.room_name=room_name
        self.method=method
        self.test=test
        self.path=path
        self.path_length=path_length
        self.operations=operations
        self.time=time
    def print_path(self):
        print("room name : " , self.room_name,", method used : ", self.method, ", test : ",self.test,", path : ",self.path, ", path length : ",self.path_length,", number of operations : ", self.operations, ", time : ", self.time)
        

