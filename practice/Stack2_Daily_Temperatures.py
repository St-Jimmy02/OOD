class Stack:
    def __init__(self, data = None):
        if data: self.stack = data
        else: self.stack = []
    def push(self, data): self.stack.append(data)
    def isEmpty(self): return not self.stack
    def pop(self): return self.stack.pop() if not self.isEmpty() else None
    def peak(self): return self.stack[-1] if not self.isEmpty() else None
    def size(self): return len(self.stack) if not self.isEmpty() else None
    def __iter__(self): return iter(self.stack)
    def __str__(self): return f"{self.stack}"


def check_temp(stack, temp, num = 0):
    if stack.isEmpty():
        return 0
    if int(temp) < stack.peak():
        return num + 1
    if int(temp) >= stack.peak():
        stack.pop()
        return check_temp(stack, temp, num + 1)

ips = list(map(int, input("Enter Input : ").split()))
res = []
for index in range(len(ips)):
    stack = Stack()
    for ip in ips[-1:index:-1]:
        stack.push(ip)
    td_temp = ips[index]
    print(stack)
    print(td_temp)
    num = check_temp(stack, td_temp)
    res.append(num)
    
print(res)