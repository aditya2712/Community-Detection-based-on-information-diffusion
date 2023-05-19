from APAL import *
from Graph import *
from OGG import *


path = "./"
filename = "15rw_"
dataset = "03"  # dataset number
edge_file = open(path + filename + "t" + str(dataset) + ".csv", "r")
edge_list = edge_file.readlines()
G = Graph()
max_node = -1
for edge in edge_list:
    edge = edge.split()
    G.add_vertex(int(edge[0]))
    G.add_vertex(int(edge[1]))
    G.add_edge(int(edge[0]), int(edge[1]))
    G.add_edge(int(edge[1]), int(edge[0]))
    max_node = max(max_node, int(edge[0]))
    max_node = max(max_node, int(edge[1]))


apal = APAL()
apal.graph = G  # the graph we have defined above
apal_clusters = apal.run_apal(0.2)
    
print(apal_clusters)
