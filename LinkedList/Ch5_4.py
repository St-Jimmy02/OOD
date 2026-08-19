class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    Angry = 0
    Worker = 0
    Army = 0

    def __init__(self, data=None):
        self.head = None
        self.size = 0

    def __str__(self):
        crr = self.head
        worker, army = [], []
        while crr:
            (worker if crr.data.startswith('W') else army).append(crr.data)
            crr = crr.next

        return (f"-> Remaining worker ants: {' '.join(worker) if len(worker)!=0 else 'Empty'}\n"
                f"-> Remaining soldier ants: {' '.join(army)if len(army)!=0 else 'Empty'}")
    
    def show(self):
        cur = self.head
        ants = []
        while cur:
            ants.append(cur.data)
            cur = cur.next
        return ' '.join(ants) if ants else 'Empty'
    
    def add_W(self, data):
        for _ in range(data):
            self.Worker += 1
            newNode = Node(f"W{self.Worker}")
            if not self.head or self.head.data.startswith('A'):
                newNode.next = self.head
                self.head = newNode
            else:
                crr = self.head
                while crr.next and crr.next.data.startswith('W'):
                    crr = crr.next
                newNode.next = crr.next
                crr.next = newNode
            self.size += 1

    def remove_W(self):
        if not self.head or self.head.data.startswith('A'): return None
        pop = self.head.data
        self.head = self.head.next
        self.Worker -= 1
        self.size -= 1
        return pop
            
    def add_A(self, data):
        for _ in range(data):
            self.Army += 1
            newNode = Node(f"A{self.Army}")
            if not self.head: self.head = newNode
            else:
                crr = self.head
                while crr.next:
                    crr = crr.next
                crr.next = newNode
            self.size += 1

    def remove_A(self):
        prev, crr = None, self.head
        while crr and crr.data.startswith('W'):
            prev, crr = crr, crr.next
        if not crr: return None
        if prev:
            prev.next = crr.next
        else:
            self.head = crr.next
        self.Army -= 1
        self.size -= 1
        return crr.data

    def carry(self, food):
        ants = []
        while food > 0:
            ant = self.remove_W()
            power = 2

            if ant is None:
                ant = self.remove_A()
                power = 5

            if ant is None:
                print(f"Food carrying mission : {' '.join(ants) if ants else 'Empty'}")
                print("The food load is incomplete!")
                self.Angry += 1
                if self.Angry == 3:
                    print("Queen is angry! ! !\n**The queen is furious! The ant colony has been destroyed**")
                    exit()
                else:
                    print("Queen is angry! ! !")
                return
            ants.append(ant)
            food -= power
        print(f"Food carrying mission : {' '.join(ants) if ants else 'Empty'}")

    def fight(self, hp):
        ants = []
        while hp > 0:
            ant = self.remove_A()
            damage = 10

            if ant is None:
                ant = self.remove_W()
                damage = 5

            if ant is None:
                print("Attack mission :", ' '.join(ants) if ants else 'Empty')
                print("Ant nest has fallen!")
                exit()

            ants.append(ant)
            hp -= damage
        print(f"Attack mission : {' '.join(ants)}")


ll = LinkedList()
start, ips = input('***This colony is our home***\nEnter input : ').split('/')
w, a = map(int, start.split())
ll.add_W(w)
ll.add_A(a)
print(f"Current Ant List: {ll.show()}\n")
for ip in ips.split(','):
    op = ip.split()

    if len(op) == 1:
        if op[0] == 'S':
            print(ll)
    else:
        command, value = op[0], int(op[1])

        if command == 'C':
            ll.carry(value)
        elif command == 'F':
            ll.fight(value)
        elif command == 'W':
            ll.add_W(value)
        elif command == 'A':
            ll.add_A(value)