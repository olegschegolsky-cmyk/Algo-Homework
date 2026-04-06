import unittest

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

class TestFindSuccessor(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTree(10)
        
        self.node_5 = BinaryTree(5)
        self.node_15 = BinaryTree(15)
        self.root.left = self.node_5
        self.root.right = self.node_15
        
        self.node_3 = BinaryTree(3)
        self.node_7 = BinaryTree(7)
        self.node_5.left = self.node_3
        self.node_5.right = self.node_7
        
        self.node_20 = BinaryTree(20)
        self.node_15.right = self.node_20
        
        self.node_12 = BinaryTree(12)
        self.node_20.left = self.node_12

    def test_successor_of_right_child(self):
        result = find_successor(self.root, self.node_7)
        self.assertEqual(result, self.root)

    def test_successor_of_left_leaf(self):
        result = find_successor(self.root, self.node_3)
        self.assertEqual(result, self.node_5)

    def test_successor_of_root(self):
        result = find_successor(self.root, self.root)
        self.assertEqual(result, self.node_15)

    def test_successor_deep_in_tree(self):
        result = find_successor(self.root, self.node_12)
        self.assertEqual(result, self.node_20)

    def test_node_with_no_successor(self):
        result = find_successor(self.root, self.node_20)
        self.assertIsNone(result)

unittest.main()