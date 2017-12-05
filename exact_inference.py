from node_clique import Node, Clique, Graph, Junction_tree_cloud
def min_fill(graph):
    nodes = graph.get_nodes()
    unvisited_nodes = set(nodes)
    while not len(unvisited_nodes) == 0:
        min_edge_fillin = len(unvisited_nodes)
        for node in unvisited_nodes:
            edge_fillin = 0
            for neighbor in node.neighbor:
                if(neighbor in unvisited_nodes):
                    for neighbor_ in node.neighbor:
                        if(neighbor_ in unvisited_nodes):
                            if(neighbor != neighbor_ and 
                               neighbor not in neighbor_.neighbor):
                                edge_fillin += 1
            if(min_edge_fillin > edge_fillin):
                min_edge_fillin = min(min_edge_fillin, edge_fillin)    
                node_elim = node
        for neighbor in node_elim.neighbor:
            if(neighbor in unvisited_nodes):
                for neighbor_ in node_elim.neighbor:
                    if(neighbor_ in unvisited_nodes):
                        if(neighbor != neighbor_):
                            neighbor.add_neighbor(neighbor_)
        unvisited_nodes.remove(node_elim)
                        
def MSC(graph):
    nodes = graph.get_nodes()
    max_cliques = []
    isvisited = [False] * len(nodes)
    pre_c = set()
    pre_node_elim = nodes[0]
    while False in isvisited:
        max_c = set()
        node_elim = nodes[0]
        for node in nodes:
            c = set()
            if(not isvisited[node.index]):
                for neighbor in node.neighbor:
                    if(isvisited[neighbor.index]):
                        c.add(neighbor)
            if(len(c) > len(max_c)):
                node_elim = node
                max_c = c
        if(len(pre_c) >= len(max_c) and len(max_c) != 0):
            pre_c.add(pre_node_elim)
            max_cliques.append(pre_c)
        isvisited[node_elim.index] = True
        pre_c = max_c
        pre_node_elim = node_elim
    pre_c.add(pre_node_elim)
    max_cliques.append(pre_c)
    max_cliques_object = []
    for clique_set in max_cliques:
        max_cliques_object.append(Clique(list(clique_set), None))
    return max_cliques_object
    
def generate_junction_tree(max_cliques):
    cliques = []
    for clique in max_cliques:
        cliques.append(Junction_tree_cloud(clique, set()))
    for i in range(0, len(cliques)):
        index = 0
        max_num_neighbor = 0
        for j in range(0, i):
            num_neighbor = len(cliques[i].nodes & cliques[j].nodes)
            if(num_neighbor > max_num_neighbor):
                max_num_neighbor = num_neighbor
                index = j
        cliques[index].neighbor.add(cliques[i])
        cliques[i].neighbor.add(cliques[index])
    return cliques[0]

def rotate_axis(clique_1, clique_2):
    index_1 = []
    index_2 = []
    for node in clique_1.nodes:
        index_1.append(node.index)
    for node in clique_2.nodes:
        index_2.append(node.index)
    print(index_1)
    print(index_2)
    left = []
    right = []
    index = 0
    for i in index_1:
        if i in index_2:
            left.append(index)
        else:
            right.append(index)
        index += 1
    left.extend(right)
    return left
        

    
            
#def initialize_table(graph, max_cliques):
#    for clique in graph.cliques:
        
         
        
    
    
    
    
    
    
    
    
    
    
                
        
    