class Stack:
    def __init__(self, data = None): 
        if data == None: self.items = []
        else: self.items = data
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if not self.is_empty() else None
    def peek(self): return self.items[-1] if not self.is_empty() else None
    def is_empty(self): return len(self.items) == 0

def infix_to_postfix(expression):
    # กําหนดลําดับความสําคัญของ operator
    precedence = {
    '^': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0
    }
    
    stack = Stack()
    output = []
    tokens = list(expression)
    for token in tokens:
        if token.isalnum():
            output.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop() # เอาวงเล็บเปิดออก
        else: # เป็น operator
            while (not stack.is_empty() and precedence[stack.peek()] >= precedence[token]):
                output.append(stack.pop())
            stack.push(token)
    while not stack.is_empty():
        output.append(stack.pop())
    return ''.join(output)

ip = input(' ***Infix to Postfix***\nEnter Infix expression : ')
print('PostFix :')
print(infix_to_postfix(ip))