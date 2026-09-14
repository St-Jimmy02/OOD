class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class Queue:
    def __init__(self, data=None):
        self.queue = []
        if data: self.queue = data
    def isEmpty(self): return len(self.queue) == 0
    def enqueue(self, data): self.queue.append(data)
    def dequeue(self): return self.queue.pop(0) if not self.isEmpty() else None
    def size(self): return len(self.queue)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        def _insert(root, data):
            if root is None: return Node(data)
            if data < root.data: root.left = _insert(root.left, data)
            elif data >= root.data: root.right = _insert(root.right, data)
            return root
        self.root = _insert(self.root, data)


    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


    def left_boundary(self, node):
        result = []
        self._left_boundary(node, result)
        return result

    def _left_boundary(self, node, result):
        if node is None:
            return
        if node.left is None and node.right is None:
            return 

        result.append(node)

        if node.left is not None:
            self._left_boundary(node.left, result)
        else:
            self._left_boundary(node.right, result)


    def right_boundary(self, node):
        result = []
        self._right_boundary(node, result)
        return result

    def _right_boundary(self, node, result):
        if node is None:
            return
        if node.left is None and node.right is None:
            return

        if node.right is not None:
            self._right_boundary(node.right, result)
        else:
            self._right_boundary(node.left, result)

        result.append(node)

    def leaves(self, node):
        result = []
        self._leaves(node, result)
        return result

    def _leaves(self, node, result):
        if node is None:
            return
        if node.left is None and node.right is None:
            result.append(node)
            return
        self._leaves(node.left, result)
        self._leaves(node.right, result)

    def boundary_traversal(self):
        if self.root is None:
            return []
        if self.root.left is None and self.root.right is None:
            return [self.root]

        result = [self.root]
        result += self.left_boundary(self.root.left)
        result += self.leaves(self.root)
        result += self.right_boundary(self.root.right)
        return result


raw = input("Enter Input : ")
values = [int(x) for x in raw.split()]

tree = BST()
for v in values:
    tree.insert(v)

tree.printTree(tree.root)

boundary = tree.boundary_traversal()
print("Boundary Traversal:", [node.data for node in boundary])