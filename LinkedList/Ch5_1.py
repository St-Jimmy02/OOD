class Node:
    def __init__(self, data, nextnode = None):
        self.data = data
        self.next = nextnode


class LinkedList:
    def __init__(self, data = None):
        self.head = None
        self.tail = None
        self.size = 0
        if data != None:
            for i in data:
                self.add_tail(i)

    def add_head(self, data):
        self.head = Node(data, self.head)
        self.size += 1

    def add_tail(self, data):
        if self.head == None: 
            self.head = Node(data, self.head)
            self.size += 1
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(data)
            self.size += 1

    def del_tail(self):
        if self.head == None:
            print('Error!!!')
            return 
        elif self.head.data != None and self.head.next == None:
            self.head = None
            self.size -= 1
            return
        else:
            current = self.head
            while current.next.next != None:
                    current = current.next
            current.next = None
            self.size -= 1

    def rename(self, name):
        if self.head == None:
            print('Error!!!')
            return 
        current = self.head
        while current.next != None:
                current = current.next
        current.data = name

    def printList(self):
        current = self.head
        if current == None:
            print('Linklist is empty!')
            return
        while current.next != None:
            print(current.data, end=' -> ')
            current = current.next
        print(current.data)

    def printListWithNoDuplicate(self):
        nodelist = []
        current = self.head
        if current == None:
            print('Linklist is empty!')
            return
        while current != None:
            if current.data not in nodelist:
                nodelist.append(current.data)
            current = current.next
        print(' -> '.join(nodelist))


def convertToLinkList(listSong):
    return LinkedList(listSong)

        
print("*** My Favourite Keynote ***")
inputl = input("Enter Input / List of operation : ").split('/')
listSong = [ele for ele in inputl[0].strip().split(' ')]
operations = [ele for ele in inputl[1].strip().split(", ")]

myLinkList = convertToLinkList(listSong)
myLinkList.printList()
for op in operations:
    if op == 'D': myLinkList.del_tail()
    elif op.startswith('A '): myLinkList.add_tail(op[2:])
    elif op.startswith('R '): myLinkList.rename(op[2:]) 
myLinkList.printList()
myLinkList.printListWithNoDuplicate()

# linkedlist = LinkedList()
# linkedlist.add_tail(10)
# linkedlist.add_tail(20)
# linkedlist.rename(30)
# linkedlist.del_tail()
# linkedlist.printList()