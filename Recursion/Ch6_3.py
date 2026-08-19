def power(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 1
    else: return a * power(a, b - 1)

a, b = input('Enter Input a b : ').split()
print(power(int(a), int(b)))