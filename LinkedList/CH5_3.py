class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self, data = None):
        self.head = None
        self.size = 0
        if data != None:
            for i in data:
                self.append(i)

    def isEmpty(self): return self.size == 0

    def append(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = newNode
        self.size += 1


def check_git_history(history_string):
    branches = []
    branch_texts = history_string.split('|')
    
    for b_text in branch_texts:
        ll = LinkedList()
        commits = b_text.split('->')
        for c in commits:
            ll.append(c.strip())
        branches.append(ll)

    first_branch = branches[0]
    crr = first_branch.head
    while crr and crr.next:
        crr = crr.next
    root_id = crr.data

    is_same_repo = True

    for i in range(1, len(branches)):
        crr = branches[i].head
        while crr and crr.next:
            crr = crr.next
            
        if crr.data != root_id:
            is_same_repo = False
            break
            
    print(f"Are these branches in the same repository? {is_same_repo}")

    if is_same_repo:
        counted_merges = LinkedList()
        merge_count = 0
        for i in range(len(branches)):
            crr1 = branches[i].head
            while crr1 and crr1.next:
                for j in range(i+1, len(branches)):
                    crr2 = branches[j].head
                    while crr2 and crr2.next:
                        if crr1.data == crr2.data and crr1.next.data != crr2.next.data:
                            is_already_counted = False
                            check_node = counted_merges.head
                            while check_node:
                                if check_node.data == crr1.data:
                                    is_already_counted = True
                                    break
                                check_node = check_node.next
                            
                            if not is_already_counted:
                                counted_merges.append(crr1.data)
                                merge_count += 1

                        crr2 = crr2.next
                crr1 = crr1.next

        print(f"{merge_count} Merge(s)")

ip = input('Git History: ').strip()
check_git_history(ip)