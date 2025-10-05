class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node):
    if not node:
        return None
    
    mapping = {}

    def dfs(node):
        if node in mapping:
            return mapping[node]
        
        clone = Node(node.val)
        mapping[node] = clone
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))
        
        return clone

    return dfs(node)

# Example usage:
# 1 -- 2
# |    |
# 4 -- 3

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

cloned_node1 = clone_graph(node1)
print(cloned_node1.val)  # Output: 1
