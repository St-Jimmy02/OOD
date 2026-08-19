class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

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
            self.head.previous = newnode
            if self.size == 1: self.tail = self.head
            self.head = newnode
        self.size += 1

    def add_tail(self, data):
        newnode = Node(data)
        if self.isEmpty():
            self.head = newnode
            self.tail = newnode
        else:
            newnode.previous = self.tail
            self.tail.next = newnode
            if self.size == 1: self.head = self.tail
            self.tail = newnode
        self.size += 1

    def insert(self, index, data):
        newnode = Node(data)
        if index < 0 or index > self.size:
            print('Data cannot be added')
        elif not self.isEmpty() and index == 0:
            self.add_head(data)
        elif not self.isEmpty() and index == self.size:
            self.add_tail(data)
        elif index > 0 and index < self.size:
            current = self.head
            for _ in range(index):
                current = current.next
            before = current.previous
            newnode.previous = before
            before.next = newnode
            current.previous = newnode
            newnode.next = current
            self.size += 1
        else: print('Data cannot be added')


    def remove_by_data(self, data): #แบบลบตัวเดียว ถ้าลบหลายตัวที่มี data เดียวกันเปลี่ยน elif เป็น if แล้วเพิ่ม self.size -= 1 ในทุกตัว
        current = self.head
        while current != None:
            if current.data == data:
                if self.head == self.tail:
                    self.head, self.tail = None
                elif current == self.head:
                    self.head = current.next
                    self.head.previous = None
                elif current == self.tail:
                    self.tail = current.previous
                    self.tail.next = None
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                self.size -= 1
            current = current.next
            return
        print('Not found')
        return
    
    def remove_by_index(self, data):
        current = self.head
        index = 0
        if data >= 0 and data < self.size:
            while data != index:
                current = current.next
                index += 1
            if self.head == self.tail and index == 0:
                self.head, self.tail = None, None
                self.size -= 1
                return
            elif data == 0:
                self.head = current.next
                self.head.previous = None
                self.size -= 1
                return
            elif data == self.size - 1:
                self.tail = current.previous
                self.tail.next = None
                self.size -= 1
                return
            current.previous.next = current.next
            current.next.previous = current.previous
            self.size -= 1
            return
        else:
            print('Not found')
            return

    def get_size(self): return self.size

    def __str__(self):
        if self.isEmpty(): return 'Null'
        current = self.head
        res = []
        while current:
            res.append(str(current.data))
            current = current.next
        return ' -> '.join(res)       


ips, N = input('Enter Input : ').strip().split(', ')
ips = ips.split(' -> ')
N = int(N.split('=')[1])
# print(ips, N)
ll = LinkedList(ips)
ll.remove_by_index(ll.get_size()-N)
print(ll)