class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    nodes = []
    
    def traverse(current):
        if current:
            traverse(current.left)
            nodes.append(current)
            traverse(current.right)
            
    traverse(tree)
    
    for i in range(len(nodes) - 1):
        if nodes[i] == node:
            return nodes[i + 1]
            
    return None

root = BinaryTree(10)

node_5 = BinaryTree(5)
node_15 = BinaryTree(15)
root.left = node_5
root.right = node_15

node_3 = BinaryTree(3)
node_7 = BinaryTree(7)
node_5.left = node_3
node_5.right = node_7

node_20 = BinaryTree(20)
node_15.right = node_20

node_12 = BinaryTree(12)
node_20.left = node_12

result = find_successor(root, node_7)

print(result.value)