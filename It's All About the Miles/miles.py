from collections import defaultdict as ddict
A, F, I, tmin, tmax = input().split()
A, F, I = map(int, [A, F, I])
tmin, tmax = map(float, [tmin, tmax])
airports = []
for _ in range(A): airports.append(input())
flights = ddict(lambda:ddict(list))
for _ in range(F):
    inp = input()
    ori, des, tdep, tarr = inp.split()
    flights[ori][des].append((float(tdep), float(tarr), inp))
iroute = []
for _ in range(I): iroute.append(input())

def prinroute(route, ct, rpr):
    if len(route)==1:
        print(rpr+'###')
        flag = 1
        return True
    ori = route[0]
    route = route[1:]
    res = []
    for ftdep, ftarr, fstr in flights[ori][route[0]]:
        if ftdep - ct < tmin or ftdep - ct > tmax:
            res.append(False)
        else:
            res.append(prinroute(route, ftarr, rpr+fstr+'\n'))
    return any(res)

if not prinroute(iroute, 0, ''): print('NO RUNS')
    