"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node):
        if not node or not node[0]: return node
        s,res = [node], { node: Node(node.val,[])}
        while s:
            n = s.pop()
            for i in n.neighbors:
                if i not in res:
                    s.append(i)
                    res[i] = Node(i.val,[])
                res[n].neighbours.append(res[i])
        return res[node]

