def meow(data):
    stack = []

    for item in data:
        item = int(item)

        if len(stack) == 0:
            stack.append(item)
        else:
            if abs(item - stack[-1]) in (5, 10) or item + stack[-1] in (5, 10):
                stack.append(item)

    return stack

ip = input("***Always 5 or 10***\nEnter Input : ").split()
print('Output :', *meow(ip))