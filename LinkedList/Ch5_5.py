class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

def createLL(LL):
    if not LL:
        return None
    head = Node(LL[0])
    curr = head
    for val in LL[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

def printLL(head):
    res = []
    curr = head
    while curr:
        res.append(str(curr.value))
        curr = curr.next
    return " ".join(res)

def SIZE(head):
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count

def bottomUp(head, b, size):
    lift = int(size * b / 100)
    if lift <= 0 or lift >= size:
        return head
    
    curr = head
    for _ in range(lift - 1):
        curr = curr.next
        
    new_head = curr.next
    curr.next = None
    
    tail = new_head
    while tail.next:
        tail = tail.next
    tail.next = head
    
    return new_head

def riffle(head, r, size):
    lift = int(size * r / 100)
    if lift <= 0 or lift >= size:
        return head
        
    curr = head
    for _ in range(lift - 1):
        curr = curr.next
        
    head2 = curr.next
    curr.next = None
    head1 = head
    
    dummy = Node(0)
    tail = dummy
    p1, p2 = head1, head2
    
    while p1 and p2:
        tail.next = p1
        p1 = p1.next
        tail = tail.next
        
        tail.next = p2
        p2 = p2.next
        tail = tail.next
        
    if p1:
        tail.next = p1
    if p2:
        tail.next = p2
        
    return dummy.next

def deriffle(head, r, size):
    lift = int(size * r / 100)
    if lift <= 0 or lift >= size:
        return head
        
    dummy1, dummy2 = Node(0), Node(0)
    t1, t2 = dummy1, dummy2
    curr = head
    c1, c2 = 0, 0
    
    while curr:
        if c1 < lift and c2 < size - lift:
            t1.next = curr
            curr = curr.next
            t1 = t1.next
            c1 += 1
            
            t2.next = curr
            curr = curr.next
            t2 = t2.next
            c2 += 1
        elif c1 < lift:
            t1.next = curr
            curr = curr.next
            t1 = t1.next
            c1 += 1
        elif c2 < size - lift:
            t2.next = curr
            curr = curr.next
            t2 = t2.next
            c2 += 1
            
    t1.next = None
    t2.next = None
    t1.next = dummy2.next
    
    return dummy1.next

def debottomUp(head, b, size):
    lift = int(size * b / 100)
    if lift <= 0 or lift >= size:
        return head
        
    cut_pos = size - lift
    curr = head
    for _ in range(cut_pos - 1):
        curr = curr.next
        
    new_head = curr.next
    curr.next = None
    
    tail = new_head
    while tail.next:
        tail = tail.next
    tail.next = head
    
    return new_head

def scarmble(head, b, r, size):
    head = bottomUp(head, b, size)
    print(f"BottomUp {b:.3f} % : {printLL(head)}")
    
    head = riffle(head, r, size)
    print(f"Riffle {r:.3f} % : {printLL(head)}")
    
    head = deriffle(head, r, size)
    print(f"Deriffle {r:.3f} % : {printLL(head)}")
    
    head = debottomUp(head, b, size)
    print(f"Debottomup {b:.3f} % : {printLL(head)}")

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)