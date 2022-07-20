''' AdjecencyList is 
    list of lists 
    node : [connected nodes]
    ...
    node : [connected nodes]
'''
class AdjecencyList:

    def __init__(self,nodes):
        self.n=nodes
        self.adjecencyList= [[]]* self.n

    def print_adjecency_list(self):
        for i in range(self.n):
            print("List of nodes of node ",format(i),"->  ",format(self.adjecencyList[i]),"\n")

    def add_node(self,connected_nodes):  
        #Find the first empty list
        for i in range(self.n):
            if not self.adjecencyList[i]:
                self.adjecencyList[i]=connected_nodes
                return 

    



