import numpy as np
import re
class Node(object):
    def __init__(self, index = None, cardinality = None, neighbor = set(), evidence = None):
        self.index = index
        self.neighbor = neighbor
        self.cardinality = cardinality
        self.evidence = evidence
        
    def get_index(self):
        return self.index
    
    def get_cardinality(self):
        return self.cardinality
    
    def get_neighbor(self):
        return self.neighbor
    
    def get_degree(self):
        return len(self.neighbor)
    
    def get_neighbor_index(self):
        neighbor_index = []
        for node in self.neighbor:
            neighbor_index.append(node.index)
        return sorted(neighbor_index)
    
    def add_neighbor(self, node):
        self.neighbor.add(node)
    
    def has_evidence(self):
        return not self.evidence is None
    
    def get_evidence(self):
        return self.evidence
    
    def set_evidence(self, val):
        self.evidence = val
    
class Clique(object):
    def __init__(self, nodes = None, table = None):
        self.nodes = nodes
        self.table = table
    
    def get_nodes(self):
        return self.nodes
    
    def get_size(self):
        return len(self.nodes)
    
    def get_table(self):
        return self.table
    
    def add_node(self, node):
        self.nodes.append(node)
        
    def set_table(self, table_list):
        node_card = []
        for node in self.nodes:
            node_card.append(node.get_cardinality())
        self.table = np.array(table_list).reshape(node_card)
        
class Graph(object):
    def __init__(self, cliques = [], nodes = []):
        self.cliques = cliques
        self.nodes = nodes
        
    def get_cliques(self):
        return self.cliques
    
    def get_cliques_num(self):
        return len(self.cliques)
    
    def get_nodes(self):
        return self.nodes
        
    def get_nodes_num(self):
        return len(self.nodes)
    
    def add_cliques(self, clique):
        self.cliques.append(clique)
    
    def add_nodes(self, node):
        self.nodes.append(node)
    
    def add_uai_evid(self, file):
        with open(file) as fid:
            data = fid.read().split('\n')
        fid.close()
        data_list = list(filter(None, data))
        data_list = list(map(int, re.split('\t|\s', data_list[0].strip())))
        del data_list[0]
        for i in range(0, len(data_list), 2):
            self.nodes[data_list[i]].set_evidence(data_list[i+1])
            
class Junction_tree_cloud(object):
    def __init__(self, nodes, neighbor, table):
        self.nodes = nodes
        self.neighbor = neighbor
        self.table = table

class Junction_tree_separator(object):
    def __init__(self, nodes, table):
        self.nodes = nodes
        self.table = table    

class Junction_tree(object):
    def __init__(self, junction_tree_clouds):
        self.junction_tree_clouds = junction_tree_clouds











          
    