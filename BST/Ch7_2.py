class Node: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, data = None):
        self.root = data

    def insert(self, data):
        def _insert(data, index = 0):
            if index >= len(data): return None
            if not is_integer(data[index]): return None

            root = Node(data[index])
            root.left = _insert(data, (2 * index) + 1)
            root.right = _insert(data, (2 * index) + 2)
            return root

        self.root = _insert(data)
        return self.root

    def check_bst(self):
        if self.root is None:
            return True
        def is_valid(node, min_val = None, max_val = None):
            if node is None:
                return True
            
            try:
                val = int(node.data)
            except (ValueError, TypeError):
                return False
            if min_val is not None and val <= min_val:
                return False
            if max_val is not None and val >= max_val:
                    return False
            return is_valid(node.left, min_val, val) and is_valid(node.right, val, max_val)

        return is_valid(self.root)

    def printing(self, root, dep: int = 0) -> None:
        if not root or str(root.data).lower() == 'null': return
        self.printing(root.right, dep+1)
        print(f"{' '*6*dep}{root.data}")
        self.printing(root.left, dep+1)

def is_integer(inp) -> bool:
    try:
        int(inp)
        return True
    except (ValueError, TypeError):
        return False


T = BST()
ip = input('Enter data stream : ').split(' ')
root = T.insert(ip)
if '' in ip: raise Exception
T.printing(root)
if T.check_bst():
    print("\nThis is valid binary search tree.")   
else:
    print("\nThis isn't valid binary search tree.")