class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}"


def printing(root: TreeNode, dep=0) -> None:
    if not root:
        return
    printing(root.right, dep + 1)
    print(f"{' ' * 6 * dep}{root.val if root.val is not None else ''}")
    printing(root.left, dep + 1)


def flatten(root: TreeNode) -> None:
    if root is None:
        return

    flatten(root.left)
    flatten(root.right)

    left_flat = root.left
    right_flat = root.right

    root.left = None
    root.right = left_flat

    current = root
    while current.right is not None:
        current = current.right

    current.right = right_flat

def build_tree(tokens):

    n = len(tokens)

    nodes = [None]
    for tok in tokens:
        if tok == "null":
            nodes.append(None)
        else:
            nodes.append(TreeNode(int(tok)))

    for i in range(1, n + 1):
        if nodes[i] is None:
            continue  # ตำแหน่งนี้ไม่มีโหนด ไม่ต้องหาลูก

        left_idx = 2 * i
        right_idx = 2 * i + 1
        if left_idx <= n:
            nodes[i].left = nodes[left_idx]
        if right_idx <= n:
            nodes[i].right = nodes[right_idx]

    return nodes[1]


raw = input("Enter Binary Tree : ")
values = [x for x in raw.split()]

root = build_tree(values)

print("Before:")
printing(root)

flatten(root)

print("After:")
printing(root)