class Stack:
    def __init__(self): self.list = []
    def push(self, data): self.list.append(data)
    def isEmpty(self): return not self.list
    def pop(self): return self.list.pop() if not self.isEmpty() else None
    def peak(self): return self.list[-1] if not self.isEmpty() else None
    def size(self): return len(self.list)
    def __str__(self): return f"{self.list}"
    def __iter__(self): return iter(self.list)


ips = list(map(int, input('Enter Input : ').split()))
for index in range(len(ips)):
    area = 0
    stack = Stack()
    stack.push(ips[index])
    if index == 0: continue
    
