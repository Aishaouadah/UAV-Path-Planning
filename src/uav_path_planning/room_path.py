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
    def path_info(self):
        path_info = "room name : " + str(self.room_name) + ", method used : " +  self.method + ", test : " + self.test + ", path : " + str(self.path) + ", path length : " + str(self.path_length) + ", number of operations : " + str(self.operations) + ", time : " + str(self.time)
        return path_info
        

