def odd_list(al):
    opls = []
    for num in al:
        if num%2 == 1: opls.append(num)
    return opls


print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
# print(ls)
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)