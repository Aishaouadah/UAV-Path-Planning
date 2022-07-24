import importlib
import sys
sys.path.append("src/uav_path_planning/adjecency_list.py")
import adjecency_list 
importlib.reload(adjecency_list) 
# THE UNUSED CODE THAT I MIGHT NEED

def image_to_adjacency_list(image):
    adjacency_list=[]
    return adjacency_list
    

# TEMPORARY CODE 

# NO Connected Nodes = -1

nodes=64
room64_000 = adjecency_list.AdjecencyList(nodes)

room64_000.add_node([1,8])
room64_000.add_node([9])
room64_000.add_node([3])
room64_000.add_node([4,11])
room64_000.add_node([5,12])
room64_000.add_node([6,13])
room64_000.add_node([14])
room64_000.add_node([15])
room64_000.add_node([9])
room64_000.add_node([17])
room64_000.add_node([11,18])
room64_000.add_node([12,19])
room64_000.add_node([-1])
room64_000.add_node([14,21])
room64_000.add_node([15,22])
room64_000.add_node([23])
room64_000.add_node([-1])
room64_000.add_node([18,25])
room64_000.add_node([-1])
room64_000.add_node([20,27])
room64_000.add_node([21,28])
room64_000.add_node([22,29])
room64_000.add_node([30])
room64_000.add_node([31])
room64_000.add_node([25,32])
room64_000.add_node([26,33])
room64_000.add_node([27,34])
room64_000.add_node([28,35])
room64_000.add_node([29,36])
room64_000.add_node([30,37])
room64_000.add_node([31])
room64_000.add_node([-1])
room64_000.add_node([33,40])
room64_000.add_node([34,41])
room64_000.add_node([35,42])
room64_000.add_node([36])
room64_000.add_node([37])
room64_000.add_node([38,45])
room64_000.add_node([39])
room64_000.add_node([47])
room64_000.add_node([41,48])
room64_000.add_node([42,49])
room64_000.add_node([43,50])
room64_000.add_node([51])
room64_000.add_node([-1])
room64_000.add_node([46,53])
room64_000.add_node([47,54])
room64_000.add_node([55])
room64_000.add_node([49,56])
room64_000.add_node([57])
room64_000.add_node([51,58])
room64_000.add_node([52,59])
room64_000.add_node([53])
room64_000.add_node([54,61])
room64_000.add_node([55])
room64_000.add_node([63])
room64_000.add_node([57])
room64_000.add_node([58])
room64_000.add_node([-1])
room64_000.add_node([-1])
room64_000.add_node([-1])
room64_000.add_node([62])
room64_000.add_node([-1])
room64_000.add_node([-1])



room64_000.print_adjecency_list()