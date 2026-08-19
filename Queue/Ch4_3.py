class Queue():
    def __init__(self): self.items = []
    def enQueue(self, data): self.items.append(data)
    def deQueue(self): return self.items.pop(0) if not self.isEmpty() else None
    def isEmpty(self): return len(self.items) == 0
    def size(self): return len(self.items)
    def __str__(self): return f"{self.items}"

ip = input("input : ").split(',')
queue = Queue()
err_dq = 0
err_ip = 0
num = 0
for i in ip:
    if i.startswith('E') and int(i[1:]) >= 0:
        num_i = int(i[1:])
        while num_i != 0:
            queue.enQueue(f"*{num}")
            num += 1
            num_i -= 1
        print(f"Step : {i}\nEnqueue : {queue}\nError Dequeue : {err_dq}\nError input : {err_ip}\n--------------------")
    elif i.startswith('D') and int(i[1:]) >= 0:
        num_i = int(i[1:])
        while num_i != 0:
            if not queue.isEmpty(): queue.deQueue()
            else: err_dq += 1
            num_i -= 1
        print(f"Step : {i}\nDequeue : {queue}\nError Dequeue : {err_dq}\nError input : {err_ip}\n--------------------")
    else:
        err_ip += 1
        print(f"Step : {i}\n{queue}\nError Dequeue : {err_dq}\nError input : {err_ip}\n--------------------")