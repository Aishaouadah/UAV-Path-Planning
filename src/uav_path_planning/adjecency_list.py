''' AdjecencyList is 
    list of lists 
    node : [connected nodes]
    ...
    node : [connected nodes]
'''

from itertools import cycle


class AdjecencyList:

    def __init__(self,nodes):
        self.n=nodes
        self.adjecencyList= [ ]* self.n

    def print_adjecency_list(self):
        
        
        for i in range(self.n):
            print("List of nodes of node {}",format(i),end="")
            temp = self.adjecencyList[i]
            while temp:
                print("-> {} ",format(temp),end="")
            print("\n")

    def add_node(self,connected_nodes):  
        self.n = self.n + 1             
        self.adjecencyList.append(connected_nodes)

    



