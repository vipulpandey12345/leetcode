"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy_of_node = Node(node.val)
            oldToNew[node] = copy_of_node
            for neigh in node.neighbors:
                copy_of_node.neighbors.append(dfs(neigh))
            return copy_of_node
        return dfs(node) if node else None
            
            
        
