num = int(input('Enter Input : '))
for i in range(0, (num+2)):
    for j in range(0, (num+2)*2):
        if j <= (num)-i: print('.',end='')
        elif j == num+2 or j == ((num+2)*2)-1 or (i == 0 and j != num+1) or (i == num+1 and j >= num+2): print('+',end='')
        else: print('#',end='')
        if j == ((num+2)*2)-1: print('')
for i in range(0, (num+2)):
    for j in range(0, (num+2)*2):
        if j >= ((num+2)*2)-i: print('.',end='')
        elif j == num+1 or (i == 0 and j <= num+1) or j == 0 or (i == num+1 and j <= num+1): print('#',end='')
        else: print('+',end='')
        if j == ((num+2)*2)-1: print('')