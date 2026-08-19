class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self): return f"prev = {self.previous.data}, data = {self.data}, next = {self.next.data}"

class DoubleLinkedList:
    def __init__(self, data = None):
        self.head = None
        self.tail = None
        self.size = 0
        if data != None:
            for i in data:
                self.append(i)

    def __str__(self): 
        current = self.head
        if current == None: return 'linked list : '
        result = []
        while current != None:
            result.append(str(current.data))
            current = current.next
        return f"linked list : {'->'.join(result)}"

    def str_reverse(self):
        current = self.tail
        if current == None: return 'reverse : '
        result = []
        while current != None:
            result.append(str(current.data))
            current = current.previous
        return f"reverse : {'->'.join(result)}"

    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
        self.size += 1

    def add_before(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.previous = newNode
            if self.size == 1: self.tail = self.head
            self.head = newNode
        self.size += 1

    def insert(self, index, data):
        newNode = Node(data)
        if index < 0 or index > self.size:
            print("Data cannot be added")
        
        elif not self.isEmpty() and index == 0:
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode
            self.size += 1
            print(f"index = 0 and data = {data}")
            
        elif self.size == 1 and index == 0:
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode
            self.tail = newNode.next
            self.size += 1
            print(f"index = 0 and data = {data}")

        elif index == self.size:
            self.append(data)
            print(f"index = {index} and data = {data}")


        elif index > 0 and index < self.size - 1:
            current = self.head
            for _ in range(index):
                current = current.next
            before = current.previous
            before.next = newNode
            newNode.previous = before
            newNode.next = current
            current.previous = newNode
            self.size += 1
            print(f"index = {index} and data = {data}")

        else: print('Data cannot be added')

    def remove(self, data):
        current = self.head
        index = 0
        while current != None:
            if current.data == data:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
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
                print(f"removed : {data} from index : {index}")
                return
            current = current.next
            index += 1
        print('Not Found!')
        return

    def debug(self):
        current = self.head
        while current:
            prev_data = current.previous.data if current.previous else None
            next_data = current.next.data if current.next else None

            print(f"prev = {prev_data}, data = {current.data}, next = {next_data}")

            current = current.next



ll = DoubleLinkedList()
ips = [ip.strip() for ip in input('Enter Input : ').split(',')]

for ip in ips:
    if ip.startswith('A '): ll.append(ip[2:])
    elif ip.startswith('Ab '): ll.add_before(ip[3:])
    elif ip.startswith('I '):
        index, data = ip[2:].split(':')
        ll.insert(int(index), data)
    elif ip.startswith('R '): ll.remove(ip[2:])
    else: print('Invalid Input!')
    print(ll)
    print(ll.str_reverse())