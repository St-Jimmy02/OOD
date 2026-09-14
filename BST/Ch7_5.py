class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def wongleb(self, data) -> list:
        data = data.strip()
        data = data.strip("[]")
        return [x.strip() for x in data.split(",")]
    def build(self, values):
        if not values or values[0] == 'null' :
            return None
        root = TreeNode(int(values[0]))
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            if i < len(values):
                if values[i] != 'null':
                    node.left = TreeNode(int(values[i]))
                    queue.append(node.left)
                i += 1
            if i < len(values):
                if values[i] != 'null':
                    node.right = TreeNode(int(values[i]))
                    queue.append(node.right)
                i += 1
        return root
    def match(self, node, t2):
        if not node:
            return False
        if not node.left and not node.right and node.val == t2.val:
            node.left = t2.left
            node.right = t2.right
            return True
        return self.match(node.left, t2) or self.match(node.right, t2)
    def check_bst(self, node, lower, upper):
        if not node:
            return True
        if not (lower < node.val < upper):
            return False
        return (self.check_bst(node.left, lower, node.val) and
                self.check_bst(node.right, node.val, upper))
    def merge(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not self.match(t1, t2):
            return None
        if not self.check_bst(t1, float('-inf'), float('inf')):
            return None
        return t1
    
    def print_tree(self, node, level=0):
        if not node:
            return
        self.print_tree(node.right, level + 1)
        print("    " * level + str(node.val))
        self.print_tree(node.left, level + 1)

i = input("Enter trees: ")
p1, p2 = i.split("/")
sol = Solution()
x = sol.wongleb(p1)
y = sol.wongleb(p2)
t1 = sol.build(x)
t2 = sol.build(y)
result = sol.merge(t1, t2)
if result:
	print("\nMerged successfully:")
	sol.print_tree(result)
else:
	print("\nCannot merge these trees.")