class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        def insert_recursive(root, data):
            if root is None: return Node(data)
            if data < root.data: root.left = insert_recursive(root.left, data)
            elif data >= root.data: root.right = insert_recursive(root.right, data)
            return root
        self.root = insert_recursive(self.root, data)
        return self.root

    def findDepth(self, node, key, depth = 0):
        if node is None: return -1
        if key == node.data: return depth
        elif key < node.data: return self.findDepth(node.left, key, depth + 1)
        elif key > node.data: return self.findDepth(node.right, key, depth + 1)
        # not found return -1

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
values = inp[:-1]
key = inp[-1]

for i in values:
    root = T.insert(i)
T.printTree(root)
print('-' * 50)
print(f"Depth of {key} : {T.findDepth(root, key)}")
