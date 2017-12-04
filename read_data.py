from node_clique import Node, Clique, Graph
import re
#%% read *.uai from disk
def read_uai(file):
    with open(file) as fid:
        data = fid.read().split('\n')
    fid.close()
    data_list = list(filter(None, data))
    # get info from data_list
    num_nodes = int(data_list[1])
    #create nodes list
    nodes_list = []
    cardinalities_list = list(map(int, re.split('\t|\s', data_list[2].strip())))
    for i in range(num_nodes):
        nodes_list.append(Node(i, cardinalities_list[i], set()))
    num_cliques = int(data_list[3])
    #create cliques list
    cliques_list = []
    for i in range(num_cliques):
        cliques_list.append(Clique([], []))
    # add clique to cliques_list
    for i in range(4, 4 + num_cliques):
        tmp = list(map(int, re.split('\t|\s', data_list[i])))
        del tmp[0]
        for index in tmp:
            node = nodes_list[index]
            cliques_list[i - 4].add_node(node)
            for index_ in tmp:
                if(index != index_):
                    node.add_neighbor(nodes_list[index_])
    # add table to cluques_list
    for i in range(5 + num_cliques, len(data_list), 2):
        tmp = list(map(float, re.split('\t|\s', data_list[i])))
        cliques_list[(i-5-num_cliques)//2].set_table(tmp)
    # create graph
    graph = Graph(cliques_list, nodes_list)
    #for node in nodes_list:
    #print(node.get_degree())
    #print(node.get_cardinality())
    #print(node.get_neighbor_index())
    return graph
    
    
if __name__ == "__main__":
    graph = read_uai("../data/3.uai")
    graph.add_uai_evid("../data/3.uai.evid")    
    
    
    
    
    
    
    
    
    
    
    
    
    