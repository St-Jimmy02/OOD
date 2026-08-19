class Stack:
    def __init__(self, data = None):
        self.stack = []
        if data: self.stack = data
    def isEmpty(self): return len(self.stack) == 0
    def push(self, data): self.stack.append(data)
    def pop(self): return self.stack.pop() if not self.isEmpty() else None
    def peek(self): return self.stack[-1] if not self.isEmpty() else None
    def size(self): return len(self.stack)

class Queue:
    def __init__(self, data = None):
        self.queue = []
        if data: self.queue = data
    def isEmpty(self): return len(self.queue) == 0
    def enqueue(self, data): self.queue.append(data)
    def dequeue(self): return self.queue.pop(0) if not self.isEmpty() else None
    def size(self): return len(self.queue)

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LL:
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        self.size = 0
        if data:
            for a in data:
                self.add_tail(a)

    def isEmpty(self): self.size == 0

    def add_head(self, data):
        newnode = Node(data)
        if self.isEmpty():
            self.head = self.tail = newnode
        else:
            newnode.next = self.head
            if self.size == 1: self.tail = self.head
            self.head = newnode
        self.size += 1

    def add_tail(self, data):
        newnode = Node(data)
        if self.isEmpty():
            self.head = self.tail = newnode
        else:
            self.tail.next = newnode
            if self.size == 1: self.head = self.tail
            self.tail = newnode

    def insert_by_index(self, index, data):
        newnode = Node(data)
        if index == 0: self.add_head(data)
        elif index == self.size - 1: self.add_tail(data)
        elif 0 < index < self.size - 1:
            crr = self.head
            for _ in range(index - 1): crr = crr.next
            newnode.next = crr.next
            crr.next = newnode

    def __str__(self):
        self.ll = []
        crr = self.head
        while crr:
            self.ll.append(crr.data)
            crr = crr,next
        return f"{' '.join(self.ll)}"

nig = LL([1, 2, 3, 4])
print(nig)
nig.insert_by_index(2, 5)
print(nig)