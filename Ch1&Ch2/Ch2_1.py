def Rshift(num,shift):
    num = num//2**shift
    if 0<num<1: return '0'
    if -1<num<0: return '0'
    return num

n,s = input("Enter number and shiftcount : ").split()
# print(bin(int(n)))
print(Rshift(int(n),int(s)))