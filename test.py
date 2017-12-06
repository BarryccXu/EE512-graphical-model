import exact_inference as EI
from read_data import read_uai
import numpy as np
#from node_clique import Node, Clique, Graph, Junction_tree_cloud



graph = read_uai("../data/test_my.uai")
EI.min_fill(graph)
max_cliques = EI.MSC(graph)
JT = EI.generate_junction_tree(max_cliques)
JT.junction_tree_clouds[0].neighbor
JT.junction_tree_clouds[1].neighbor



EI.initialize_table(JT, graph)
'''
JT.junction_tree_clouds[0].table
JT.junction_tree_clouds[0].nodes[0].index
JT.junction_tree_clouds[0].nodes[1].index
JT.junction_tree_clouds[1].table
JT.junction_tree_clouds[1].nodes[0].index
JT.junction_tree_clouds[1].nodes[1].index
'''



jt_map = EI.JT_neighbor_map(JT)

EI.mpp_forward(JT.junction_tree_clouds[0],jt_map)
np.sum(JT.junction_tree_clouds[0].table)
