class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data = None):
        self.head = None
        self.tail = None
        self.size = 0
        if data:
            for i in data: self.add_tail(i)

    def isEmpty(self): return self.size == 0

    def add_head(self, data):
        newnode = Node(data)
        if self.isEmpty():
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        self.size += 1

    def add_tail(self, data):
        newnode = Node(data)
        if self.isEmpty():
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.size += 1

    def del_tail(self):
        if self.head == self.tail:
            self.head, self.tail = None, None
        else:
            crr = self.head
            while crr.next != self.tail:
                crr = crr.next
            self.tail = crr
            self.tail.next = None
        self.size -= 1

    def del_head(self):
        if self.head == self.tail:
            self.head, self.tail = None, None
        else:
            self.head = self.head.next
        self.size -= 1

    def insert(self, data, index):
        if index == 0:
            self.add_head(data)
        elif index == self.size - 1:
            self.add_tail(data)
        elif 0 < index < self.size - 1:
            newnode = Node(data)
            crr = self.head
            crr_index = 0
            while crr_index != index:
                crr = crr.next
                crr_index += 1
            newnode.next = crr.next
            crr.next = newnode
            self.size += 1
        else: print('Not Found')

    def __str__(self):
        if self.isEmpty(): return 'Null'
        current = self.head
        res = []
        while current:
            res.append(str(current.data))
            current = current.next
        return ' -> '.join(res)


ips = input('Enter Input : ').split()
ll = LinkedList(ips)
ll.del_head()
ll.del_tail()
ll.insert(6, 1)
print(ll)