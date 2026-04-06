class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1

class AVLPriorityQueue:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, value, priority):
        self.root = self._insert(self.root, value, priority)

    def _insert(self, node, value, priority):
        if not node:
            return Node(value, priority)

        if priority >= node.priority:
            node.left = self._insert(node.left, value, priority)
        else:
            node.right = self._insert(node.right, value, priority)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and priority >= node.left.priority:
            return self.right_rotate(node)
        if balance < -1 and priority < node.right.priority:
            return self.left_rotate(node)
        if balance > 1 and priority < node.left.priority:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and priority >= node.right.priority:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def peek(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.value, current.priority

    def extract_max(self):
        if not self.root:
            return None
        self.root, deleted_node = self._pop_leftmost(self.root)
        return deleted_node.value, deleted_node.priority

    def _pop_leftmost(self, node):
        if not node.left:
            return node.right, node
        
        node.left, deleted_node = self._pop_leftmost(node.left)
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node), deleted_node
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node), deleted_node
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node), deleted_node
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node), deleted_node

        return node, deleted_node