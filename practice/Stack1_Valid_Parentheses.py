class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data): self.stack.append(data)
    def isEmpty(self): return not self.stack
    def pop(self): return self.stack.pop() if not self.isEmpty() else None
    def peak(self): return self.stack[-1] if not self.isEmpty() else None
    def size(self): return len(self.stack)
    def __str__(self): return f"{self.stack}"
    def __iter__(self): return iter(self.stack)

ips = list(input('Enter Input : ').strip())
stack = Stack()
# print(ips)
for ip in ips:
    if stack.isEmpty():
        stack.push(ip)
    elif ip == '(' or ip == '[' or ip == '{':
        stack.push(ip)
    elif (stack.peak() == '(' and ip == ')') or (stack.peak() == '[' and ip == ']') or (stack.peak() == '{' and ip == '}'):
        stack.pop()
    else:
        print('False')
        quit()
    # print(stack)
if not stack.isEmpty(): print('False')
else: print('True')