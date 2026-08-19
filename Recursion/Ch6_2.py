def pop_mood(data, crr_num, ans):
    if crr_num != '':
        ans.add(int(crr_num))

    for index in range(len(data)):
        picked_num = data[index]

        leftovers = data.copy()
        leftovers.pop(index)

        new_num = crr_num + picked_num

        pop_mood(leftovers, new_num, ans)


ip = input('Enter digits : ').split()
for i in ip:
    if not i.isdigit() or len(i) != 1:
        print('Invalid input')
        exit()
ans = set()
pop_mood(ip, '', ans)
final_ans = list(ans)
final_ans.sort()
print(f"Output : {final_ans}")