class Queue:
    def __init__(self, data=None):
        if data == None: self.items = []
        else: self.items = data
    def isEmpty(self): return len(self.items) == 0
    def enQueue(self, data): self.items.append(data)
    def deQueue(self): return self.items.pop(0) if not self.isEmpty() else None
    def size(self): return len(self.items)
    def items(self): return self.items

class Stack:
    def __init__(self, data=None):
        if data == None: self.items = []
        else: self.items = data
    def isEmpty(self): return len(self.items) == 0
    def size(self): return len(self.items)
    def push(self, data): self.items.append(data)
    def pop(self): return self.items.pop() if not self.isEmpty() else None
    def peek(self): return self.items[-1] if not self.isEmpty() else None


main_deck_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

main_deck = Queue(main_deck_list)

ip = input("Enter Commands: ").split(',')

print("\n-------------------- Original Deck -------------------")
print(f"| {' | '.join(main_deck.items)} |")

for command in ip:
    command = command.strip()
    # print(command)
    try: 
        num = int(command[1:])
        if num <= 0: raise ValueError
    except ValueError:
        print("\n-------------------- Invalid Number ------------------")
        continue

    if command.startswith('O '):
        temp_stack = Stack()
        for _ in range(num): temp_stack.push(main_deck.deQueue())
        while not temp_stack.isEmpty(): main_deck.enQueue(temp_stack.pop())
        print("\n--------------- Reverse Overhand Shuffle -------------")
        print(f"| {' | '.join(main_deck.items)} |")

    elif command.startswith('H ') and num <= 11:
        temp_stack = Stack()
        main_stack = Stack()
        while not main_deck.isEmpty():
            main_stack.push(main_deck.deQueue())
        for i in range(num, 0, -1):
            temp_stack = Stack()
            for _ in range(i):
                if not main_stack.isEmpty(): temp_stack.push(main_stack.pop())
            while not temp_stack.isEmpty(): main_deck.enQueue(temp_stack.pop())
        temp_stack = Stack()
        while not main_stack.isEmpty(): temp_stack.push(main_stack.pop())
        while not temp_stack.isEmpty(): main_deck.enQueue(temp_stack.pop())
        print("\n-------------- Decreasing Hindu Shuffle --------------")
        print(f"| {' | '.join(main_deck.items)} |")

    elif command.startswith('R '):
        print("\n------------------- Riffle Shuffle -------------------")
        for _ in range(num):
            queue1 = Queue()
            queue2 = Queue()
            half = (main_deck.size() + 1) // 2
            for _ in range(half): queue1.enQueue(main_deck.deQueue())
            while not main_deck.isEmpty(): queue2.enQueue(main_deck.deQueue())
            while not queue1.isEmpty() or not queue2.isEmpty():
                if not queue1.isEmpty(): main_deck.enQueue(queue1.deQueue())
                if not queue2.isEmpty(): main_deck.enQueue(queue2.deQueue())
            print(f"| {' | '.join(main_deck.items)} |")

    else: print("\n-------------------- Invalid Number ------------------")