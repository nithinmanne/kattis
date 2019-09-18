from collections import defaultdict as ddict
n = int(input())
loc = ddict(lambda:0)
for _ in range(n):
    a, n = input().split()
    if a=='entry':
        if loc[n] == 0:
            print(f'{n} entered')
        else:
            print(f'{n} entered (ANOMALY)')
        loc[n] = 1
    else:
        if loc[n] == 1:
            print(f'{n} exited')
        else:
            print(f'{n} exited (ANOMALY)')
        loc[n] = 0