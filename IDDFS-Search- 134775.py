# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 18:35:35 2022

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
  'N': []   
}

path = list()

def DFS(currentNode,destination,graph,maxDepth):
    print("Checking for destination",currentNode)
    
    if currentNode==destination:
        return True
    if maxDepth<=0:
        
        return False
    for node in graph[currentNode]:
        if DFS(node,destination,graph,maxDepth-1):
            return True
    return False

def iterativeDDFS(currentNode,destination,graph,maxDepth):
    for i in range(maxDepth):
        if DFS(currentNode,destination,graph,i):
            return True
    return False

if not iterativeDDFS('J','N',graph,4):
    print("Path is not available")
else:
    print("A path exists")
    print(path.pop())


