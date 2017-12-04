from node_clique import Node, Clique, Graph
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
                        
            
        
    