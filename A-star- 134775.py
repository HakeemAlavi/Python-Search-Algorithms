# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:34:12 2022

@author: 134775 HAKEEM ALAVI
"""
def aStarAlgo(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}               #store distance from starting node
    parents = {}         # parents contains an adjacency map of all nodes
    #distance of starting node from itself is zero
    g[start_node] = 0
    #start_node is root node i.e it has no parent nodes
    #so start_node is set to its own parent node
    parents[start_node] = start_node
    while len(open_set) > 0:
        n = None
        #node with lowest f() is found
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                #nodes 'm' not in first and last set are added to first
                #n is set its parent
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                #for each node m,compare its distance from start i.e g(m) to the
                #from start through n node
                else:
                    if g[m] > g[n] + weight:
                        #update g(m)
                        g[m] = g[n] + weight
                        #change parent of m to n
                        parents[m] = n
                        #if m in closed set,remove and add to open
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == None:
            print('Path does not exist!')
            return None
        
        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('A* Search solution is: {}'.format(path))
            return path
        # remove n from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None

#define fuction to return neighbor and its distance
#from the passed node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
    
#for simplicity we ll consider heuristic distances given
#and this function returns heuristic distance for all nodes
def heuristic(n):
    H_dist = {
        'A': 221,
        'B': 350,
        'C': 400,
        'D': 326,
        'E': 500,
        'F': 209,
        'G': 188,
        'H': 92,
        'I': 499,
        'J': 621,
        'K': 688,
        'L': 300,
        'M': 78,
        'N': 0,
        'O': 170,
    }
    return H_dist[n]

#Describe your graph here
Graph_nodes = {
    'A': [('O', 151), ('D', 43)],
    'B': [('G', 171)],
    'C': [('D', 126), ('B', 171)],
    'D': [('O', 136), ('M', 200), ('F', 111)],
    'E': [('L', 110), ('A', 133)],
    'F': [('G', 88), ('H', 130)],
    'G': [('C', 140), ('D', 123), ('H', 99)],
    'H': [('N', 80)],
    'I': [('A', 109), ('C', 102)],
    'J': [('K', 146), ('E', 105), ('I', 172)],
    'K': [('E', 146), ('L', 152)],
    'L': [('O', 97)],
    'M': [('N', 67)],
    #'N':[],
    'O': [('M', 100)],
}

aStarAlgo('J', 'N')
    