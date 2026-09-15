class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.Height = 1
        self.setHeight()

    def getHeight(self, node):
        return -1 if node is None else node.height

    def setHeight(self):
        self.height = 1 + max(self.getHeight(self.left), self.getHeight(self.right))
        return self.height

    def balanceValue(self):
        return self.getHeight(self.left) + self.getHeight(self.right)
    
    def __str__(self):
        return str(self.data)

class AVL:
    def __init__(self, root, data = None):
        self.root = None

    def LL(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        x.setHeight()
        y.setHeight()
        return y

    def RR(self, x):
        y = x.left
        x.right = y.left
        y.left = x
        x.setHeight()
        y.setHeight()
        return y

    def LR(self, x):
        x.left = self.RR(x.left)
        return self.LL(x)

    def RL(self, x):
        x.right = self.LL(x.right)
        return self.RR(x)

    def reBalance(self, x):
        if x is None: return x
        x.setHeight()
        bf = x.balanceValue()
        if bf > 1:
            if x.left.balanceValue() > 0:
                x = self.LL(x)
            else:
                x = self.LR(x)
        elif bf < -1:
            if x.right.balanceValue() < 0:
                x = self.RR(x)
            else:
                x = self.RL(x)
        x.setHeight()
        return x




    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    ?????