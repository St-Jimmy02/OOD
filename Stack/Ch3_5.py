class Stack:
    def __init__(self, data=None):
        if data == None: self.items = []
        else: self.items = data
    def push(self, data): self.items.append(data)
    def pop(self): return self.items.pop() if not self.is_empty() else None
    def peek(self): return self.items[-1] if not self.is_empty() else None
    def size(self): return len(self.items)
    def __str__(self): return f"{self.items}\n{len(self.items)}"
    def __iter__(self): return iter(self.items)
    def is_empty(self): return len(self.items) == 0


def waer(ip):
    stack = Stack()
    Water = 0
    for i in range(len(ip)):
        # print(stack, Water)
        if stack.is_empty() or ip[stack.peek()] >= ip[i]:
            stack.push(i)
        else: 
            while ip[stack.peek()] < ip[i]:
                Bottom = stack.pop()
                if stack.is_empty(): break
                L_wall = stack.peek()
                R_wall = i
                # print(Bottom, L_wall, R_wall)
                Weight = R_wall - L_wall - 1
                Height = min(ip[L_wall], ip[R_wall]) - ip[Bottom]
                Water += Weight * Height
                # print(Water)
            stack.push(i)
    return Water


ip = list(map(int, input(' *** Trap Water *** \nInput heights : ').split()))
print('Trapped Water:', waer(ip))


    # L_wall = []
    # R_wall = []
    # for num in ip:
    #     min = 0
    #     if num > min:
    #         min = num
    #         L_wall.append(min)
    #     else: 
    #         L_wall.append(min)
    # for num in reversed(ip):
    #     min = 0
    #     if num > min:
    #         min = num
    #         R_wall[:0] = [min]
    #     else: 
    #         R_wall[:0] = [min]
    
    # L_water = [] # x-y for x, y in zip(L_wall, ip)
    # R_water = [] # x-y for x, y in zip(R_wall, ip)
    # for x, y in zip(L_wall, ip):
    #     if 

