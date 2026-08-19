class Stack:
    def __init__(self, data = None): 
        if data == None: self.items = []
        else: self.items = data
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if not self.is_empty() else None
    def peek(self): return self.items[-1] if not self.is_empty() else None
    def is_empty(self): return len(self.items) == 0
    def size(self): return len(self.items)
    def __iter__(self): return iter(self.items)

bar = Stack()
plates = [25, 20, 15, 10, 5, 2.5, 1.25]

ip = input('Enter needed weight(s): ').split()
for Weight in ip:
    Weight = float(Weight)
    if Weight < 20 or Weight > 270 or (Weight - 20) % 2.5 != 0:
        print(f"It's impossible to achieve the weight you want({Weight:g}).")
        break
        
    else:
        sol = []
        while (sum(sol)*2)+20 != Weight:
            for plate in plates:
                if ((sum(sol)*2)+20) + (plate*2) <= Weight:
                    sol.append(plate)
                    break
                else: continue
        if len(sol) > 5:
            print(f"It's impossible to achieve the weight you want({Weight:g}).")
            break

        match_index = 0
        while match_index < bar.size() and match_index < len(sol) and bar.items[match_index] == sol[match_index]:
            match_index += 1
        PO = []
        PU = []
        while bar.size() > match_index: # หา PO
            PO.append(bar.pop())

        for i in range(match_index, len(sol)): # หา PU
            plate = sol[i]
            PU.append(plate)
            bar.push(plate)

        for O in PO: print(f"PO:{O} ", end='')
        for U in PU: print(f"PU:{U} ", end='')
        L = ["-"] * (5 - bar.size())
        for p in reversed(bar.items):
            L.append(f"[{p}]")

        R = []
        for p in bar:
            R.append(f"[{p}]")
        R += ["-"] * (5 - bar.size())

        W_now = (sum(bar.items) * 2) + 20
        if bar.size() == 0 and len(PO) == 0:
            print(f"{''.join(L)}|======|{''.join(R)} => {W_now} KG.")
        else:
            print(f"=> {''.join(L)}|======|{''.join(R)} => {W_now} KG.")