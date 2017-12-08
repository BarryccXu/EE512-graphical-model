from node_clique import Node, Clique, Graph, Junction_tree_cloud, Junction_tree_separator, Junction_tree
import numpy as np
def min_fill(graph):
    '''
    the min-fill-in algorithm is to triangluate the graph
    '''
    nodes = graph.get_nodes()
    unvisited_nodes = set(nodes)
    while not len(unvisited_nodes) == 0:
        min_edge_fillin = len(unvisited_nodes)
        node_elim = Node(None)
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
    '''
    
    '''
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
            max_cliques.append(list(pre_c))
        isvisited[node_elim.index] = True
        pre_c = max_c
        pre_node_elim = node_elim
    pre_c.add(pre_node_elim)
    max_cliques.append(pre_c)
    max_cliques_objects = []
    # get cardinality from nodes to generate table
    cardi_list = []
    for clique in max_cliques:
        tmp = []
        for node in clique:
            tmp.append(node.cardinality)
        cardi_list.append(tmp)
    for i in range(len(max_cliques)):
        max_cliques_objects.append(Clique(list(max_cliques[i]), np.ones(cardi_list[i])))        
    return max_cliques_objects
    
def generate_junction_tree(max_cliques):
    '''
    add neigbors for each cloud
    '''
    cliques = []
    for i, clique in enumerate(max_cliques):
        tmp = []
        for node in clique.nodes:
            tmp.append(node.index)
        cliques.append(Junction_tree_cloud(i, clique.nodes, tmp, list(), clique.table))
    #generate neighbors for junction cloud
    for i in range(1, len(cliques)):
        index = 0
        max_num_neighbor = 0
        for j in range(0, i):
            num_neighbor = len(set(cliques[i].nodes) & set(cliques[j].nodes))
            if(num_neighbor > max_num_neighbor):
                max_num_neighbor = num_neighbor
                index = j
        cliques[index].neighbor.append(cliques[i])
        cliques[i].neighbor.append(cliques[index])
    return Junction_tree(cliques)

def rotate_axis(cloud, clique):

    index_1 = cloud.nodes_index
    index_2 = []
    for node in clique.nodes:
        index_2.append(node.index)
    #print(index_1)
    #print(index_2)
    index_2_map = {}
    delta_index = len(index_1) - len(index_2)
    for i in range(len(index_2)):
        index_2_map[index_2[i]] = i + delta_index
    #print(index_2_map)
    rotated_axis = []
    index = 0
    for num in index_1:
        if num in index_2_map:
            rotated_axis.append(index_2_map[num])
        else:
            rotated_axis.append(index)
            index += 1
    return rotated_axis

def update_table(clique_1, clique_2):
    rotate = rotate_axis(clique_1, clique_2)
    table_1 = clique_1.table
    table_2 = clique_2.table
    table_1_rotated = np.moveaxis(table_1, range(len(clique_1.nodes)), rotate)
    table_1_rotated = table_1_rotated * table_2
    table_1 = np.moveaxis(table_1_rotated, rotate, range(len(clique_1.nodes)))
    clique_1.table = table_1
            
def initialize_table(junction_tree, graph):
    '''
    initialize tables in the junction_tree_cloud based on tables from given '.uai' file
    '''
    for clique in graph.cliques:
        for cloud in junction_tree.junction_tree_clouds:
            if(set(clique.nodes).issubset(set(cloud.nodes))):
                update_table(cloud, clique)
                break

def separator_sum_index(cloud, separator):
    index_c = cloud.nodes_index
    index_s = []
    idx = []
    for node in separator.nodes:
        index_s.append(node.index)
    for i in range(len(index_c)):
        if index_c[i] not in index_s:
            idx.append(i)
    return tuple(idx)

def JT_neighbor_map(junction_tree):
    jt_map = dict()
    for cloud in junction_tree.junction_tree_clouds:
        jt_map[cloud.index] = set(cloud.get_neighbor_index())
    return jt_map

def mpp_forward(root, jt_map):
    if(len(jt_map[root.index]) == 0):
        return
    for child in root.neighbor:
        if (child.index in jt_map[root.index]):
            jt_map[root.index].remove(child.index)
            jt_map[child.index].remove(root.index)
            mpp_forward(child, jt_map)
            separator = Junction_tree_separator([i for i in child.nodes if i in root.nodes],
                                                np.array([]))
            idx = separator_sum_index(child, separator)
            separator.table = np.sum(child.table, axis = idx)
            update_table(root, separator)
            #print(root)
    
    
            
    
    
    
    
    
    
    
    
    
    
                
        
    