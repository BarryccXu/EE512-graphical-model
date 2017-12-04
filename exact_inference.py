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
    return max_cliques
    
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
            
        
        
    
    
    
    
    
    
    
    
    
    
                
        
    