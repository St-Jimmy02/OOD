class Queue:
    def __init__(self): self.items = []
    def enQueue(self, data): self.items.append(data)
    def deQueue(self): return self.items.pop(0) if not self.isEmpty() else None
    def isEmpty(self): return len(self.items) == 0
    def size(self): return len(self.items)
    def __str__(self): return ", ".join(map(str, self.items)) if not self.isEmpty() else 'Empty'

ip = input("Enter Input : ").split(',')
queue = Queue()
Out = []
for token in ip:
    if token.startswith('E '): 
        queue.enQueue(int(token[2:]))
        print(queue)
    elif token == 'D':
        if queue.isEmpty(): print('Empty')
        else:
            love = queue.deQueue()
            Out.append(love)
            print(f"{love} <- {queue}")

if len(Out) == 0: Out = 'Empty'
else: Out = ", ".join(map(str, Out))
print(f"{Out} : {queue}")