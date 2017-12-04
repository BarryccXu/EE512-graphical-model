import exact_inference as EI
from read_data import read_uai
#from node_clique import Node, Clique, Graph, Junction_tree_cloud


graph = read_uai("../data/test.uai")
EI.min_fill(graph)
for node in graph.nodes:
    print(node.get_neighbor_index())

max_cliques = EI.MSC(graph)
for clique in max_cliques:
    print("------------------")
    for node in clique:
        print(node.index)

clouds = EI.generate_junction_tree(max_cliques)

for cloud in clouds:
    print(cloud.neighbor)