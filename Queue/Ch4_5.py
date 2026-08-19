class Queue:
    def __init__(self, data=None): 
        if data == None: self.items = []
        else: self.items = data
    def isEmpty(self): return len(self.items) == 0
    def enQueue(self, data): self.items.append(data)
    def deQueue(self):return self.items.pop(0) if not self.isEmpty() else None
    def size(self): return len(self.items)


ip = input(' ***Queue of Queue of Queue of ...*** \nEnter Input : ').split(',')
main_queue = Queue()


for command in ip:
    command = command.strip()
    if command.startswith('en '):
        try:
            num_str = command.split()[1]
            num = int(num_str)
            org_id = num_str[0]
            if num <= 0: raise ValueError
        except ValueError:
            print('Invalid Input!')
            continue

        found = False
        for sub_queue in main_queue.items:
            if not sub_queue.isEmpty() and str(sub_queue.items[0])[0] == org_id:
                sub_queue.enQueue(num)
                found = True
                break

        if not found:
            new_sub_queue = Queue()
            new_sub_queue.enQueue(num)
            main_queue.enQueue(new_sub_queue)
        print(f"Enqueued: {num}")

        state = [sq.items for sq in main_queue.items]
        print(f"Queue state: {state}")

    elif command == 'de':
        if main_queue.isEmpty():
            print("Queue is empty")
        else:
            first_sub_queue = main_queue.items[0]
            dequeued_data = first_sub_queue.deQueue()

            if first_sub_queue.isEmpty():
                main_queue.deQueue()
            print(f"Dequeued: {dequeued_data}")
            state = [sq.items for sq in main_queue.items]
            print(f"Queue state: {state}")