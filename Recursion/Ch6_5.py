def asteroid_collision(asts):
    return run(asts, [])

def run(asts, stack):
    if not asts:
        return stack
    return run(asts[1:], boom(stack, asts[0]))

def boom(stack, ast):
    if not stack:
        return stack + [ast]
    top = stack[-1]
    if top >= 0 and ast <= 0:
        if top == -ast: return stack[:-1]
        elif top > -ast: return stack
        else: return boom(stack[:-1], ast)
    else: return stack + [ast]

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))