voter = int(input('*** Election ***\nEnter a number of voter(s) : '))
vote = input().split(' ')
if len(vote) > voter: raise ValueError
candidate = {}
for v in vote:
    if int(v) <= 0 or int(v) > 20: continue
    if not candidate.get(int(v)):
        candidate[int(v)] = 1
    else:
        candidate[int(v)] += 1

all_winner = [k for k, v in candidate.items() if v == max(candidate.values())]
all_winner.sort()
if not all_winner: print('*** No Candidate Wins ***')
print(' '.join(str(int(w)) for w in all_winner))


# winner = max(candidate, key=candidate.get) #key with the highest value
