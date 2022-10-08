# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 15:51:15 2022

@author: 134775 HAKEEM ALAVI
"""
graph = {
  'J': ['K', 'E', 'I'],
  'K':['E', 'L'],
  'E':['L', 'A'],
  'I':['A', 'C'],
  'A':['O', 'D'],
  'L':['O'],
  'C':['D', 'B'],
  'B':['G'],
  'D':['O', 'M', 'F'],
  '0':['M'],
  'G':['C', 'D', 'H'],
  'F':['G', 'H'],
  'M':['N'],
  'H':['N'],
 #'N': []   
}

def dfs(graph, start, goal):
    visited = []
    stack = [[start]]
    while stack:
        path = stack.pop()
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for node2 in adjacent_nodes:
                new_path = path.copy()
                new_path.append(node2)
                stack.append(new_path)
                
solution = dfs(graph, 'J', 'N')
print('Depth First Search solution is', solution)

