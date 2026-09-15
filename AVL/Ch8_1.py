class AVLNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 0
        
        self.setHeight() # คํานวณครั)งแรกจากลูก
    def getHeight(self, node):
        # หัวใจของทุกอย่าง : NULL มี height = -1
        return -1 if node is None else node.height

    def setHeight(self):
        # คํานวณ height ของตัวเองใหม่จากลูกทั)งสอง -- O(1)
        self.height = 1 + max(self.getHeight(self.left),
        self.getHeight(self.right))
        return self.height

    def balanceValue(self):
        # BF = h(ซ้าย) - h(ขวา) -> + หนักซ้าย / - หนักขวา
        return self.getHeight(self.left) - self.getHeight(self.right)

class AVLTree:
    def __init__(self, data = None):
        self.root = None
        self.size = 0
        if data:
            for _ in data:
                self.add(_)
    
    def search(self, root, key):
        while root is not None: # วนลูป ไม่กิน stack
            if key == root.data: return root
            root = root.left if key < root.data else root.right
        return None

    def LeftRotate(self, x):
        # ยกลูกซ้ายขึ*นแทน x -- ใช้กับ Case 1 (LL)
        y = x.left
        x.left = y.right # T2 ย้ายมาเป็นลูกซ้ายของ x
        y.right = x # x ลงมาเป็นลูกขวาของ y
        x.setHeight() # x ก่อนเสมอ !
        y.setHeight()
        return y # y = root ใหม่ของ subtree

    def RightRotate(self, x):
        # ยกลูกขวาขึ*นแทน x -- ใช้กับ Case 3 (RR)
        y = x.right
        x.right = y.left
        y.left = x
        x.setHeight()
        y.setHeight()
        return y

    def doubleLeft(self, x): # Case 2 (LR)
        x.left = self.RightRotate(x.left)
        return self.LeftRotate(x)

    def doubleRight(self, x): # Case 4 (RL)
        x.right = self.LeftRotate(x.right)
        return self.RightRotate(x)

    def rebalance(self, x):
        if x is None: return x
        x.setHeight() # อัปเดต height ก่อนอ่าน BF
        bf = x.balanceValue() # bf = h(ซ้าย) - h(ขวา)
        if bf == 2: # หนักซ้าย
            if x.left.balanceValue() < 0: # หักศอก (LR)
                x = self.doubleLeft(x) # Case 2
            else: # เส้นตรง (LL)
                x = self.LeftRotate(x) # Case 1
        elif bf == -2: # หนักขวา
            if x.right.balanceValue() > 0: # หักศอก (RL)
                x = self.doubleRight(x) # Case 4
            else: # เส้นตรง (RR)
                x = self.RightRotate(x) # Case 3
        x.setHeight()
        return x

    def add(self, data):
        self.root = self._add(self.root, data)
        self.size += 1 # อย่าลืมรับค่ากลับ!
    def _add(self, root, data):
        # --- ขาลง : หาทีว่าง ---
        if root is None:
            return AVLNode(data) # เจอทีDว่าง -> สร้าง leaf ใหม่
        if data < root.data:
            root.left = self._add(root.left, data)
        else: # data >= root.data -> ไปขวา
            root.right = self._add(root.right, data)
            # --- ขากลับ : ซ่อมทุก node ทีDผ่านมา ---
        return self.rebalance(root)

    def _findMin(self, node):
        if node is None or node.left is None:
            return node
        return self._findMin(node.left)

    def _remove(self, root, data):
        if root is None: return None
        if data < root.data:
            root.left = self._remove(root.left, data)
        elif data > root.data:
            root.right = self._remove(root.right, data)
        else:
            if root.left is None: return root.right
            if root.right is None: return root.left
            s = self._findMin(root.right) # successor
            root.data = s.data
            root.right = self._remove(root.right, s.data)
            self.size -= 1
        return self.rebalance(root) # เหมือน add()

    def getSize(self, node):
        return 0 if node is None else node.size

    def min_th(self, root, rank):
        self._current_rank = 0
        self._ans = None
        self._inorder_search(root, rank)
        return self._ans

    def _inorder_search(self, root, rank):
        if root is None or self._ans is not None: return
        self._inorder_search(root.left, rank)
        if self._ans is None:
            self._current_rank += 1
            if self._current_rank == rank:
                self._ans = root.data
                return
        self._inorder_search(root.right, rank)


count, num, rank = input('*** Simple but more ***\ninput  N node, Data, K small : ').split(',')
ttt = AVLTree()
num = num.split()
for n in range(int(count)):
    if num[n]: ttt.add(int(num[n]))
print(ttt.min_th(ttt.root, int(rank)))