class Queue():
    def __init__(self, ): self.items = []
    def enQueue(self, data): self.items.append(data)
    def deQueue(self): return self.items.pop(0) if not self.isEmpty() else 0
    def isEmpty(self): return len(self.items) == 0
    def size(self): return len(self.items)
    def __str__(self): return f"{self.items}"

ip = list(input("Enter people : "))
main = Queue()
cas_1 = Queue()
cas_2 = Queue()
for al in ip:
    main.enQueue(al)

for i in range(main.size()):
    if i != 0 and i%3 == 0: cas_1.deQueue()
    if i != 5 and i%2 == 1: cas_2.deQueue()
    if cas_1.size() < 5: cas_1.enQueue(main.deQueue())
    elif cas_1.size() >= 5 and cas_2.size() < 5: cas_2.enQueue(main.deQueue())
    else: continue
    print(f"{i+1} {main} {cas_1} {cas_2}")