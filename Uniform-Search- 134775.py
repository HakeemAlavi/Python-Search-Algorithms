# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 13:36:06 2022

@author: 134775 HAKEEM ALAVI
"""

graph = {
    'J': [('K', 146), ('E', 105), ('I', 172)],
    'K':[('E', 146), ('L', 152)],
    'E':[('L', 110), ('A', 133)],
    'I':[('A', 109), ('C', 102)],
    'A':[('O', 151), ('D', 43)],
    'L':[('O', 97)],
    'C':[('D', 126), ('B', 171)],
    'B':[('G', 171)],
    'D':[('O', 136), ('M', 200), ('F', 111)],
    '0':[('M', 100)],
    'G':[('C', 140), ('D', 123), ('H', 99)],
    'F':[('G', 88), ('H', 130)],
    'M':[('N', 67)],
    'H':[('N', 80)],
    #'N': []    
    }

def path_cost(path):
    total_cost = 0
    for (node, cost) in path:
        total_cost += cost
    return total_cost, path[-1][0]


#path = [('J', 0), ('D', 5), ('G', 5)]
#print(path_cost(path))

#path = [('J', 0), ('B', 3), ('D', 4)]
#print(path_cost(path))



def ucs(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)
                
solution = ucs(graph, 'J', 'N')
print('Uniform Cost Search solution is' , solution)
print('Cost of solution is' , path_cost(solution))

                

