class Queue:
    def __init__(self, data = None):
        self.queue = []
        if data: self.queue = data
    def enQueue(self, data): self.queue.append(data)
    def isEmpty(self): return not self.queue
    def deQueue(self): return self.queue.pop(0) if not self.isEmpty() else None
    def size(self): return len(self.queue)

ips = Queue(input('Enter Input : ').split())
K = int(input('Enter K : '))
real_K = K % ips.size()
for _ in range(real_K):
    ips.deQueue()
print(f"{ips.deQueue()}")