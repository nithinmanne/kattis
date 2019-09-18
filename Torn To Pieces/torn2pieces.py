from collections import defaultdict as ddict

N = int(input())

smap = ddict(set)

for _ in range(N):
    a, *b = input().split()
    for i in b:
        smap[a].add(i)
        smap[i].add(a)

a, b = input().split()

def minpath(a, b, path):
    if b in smap[a]:
        path.append(b)
        return (1, path)
    paths = []
    for i in smap[a]:
        if i in path: continue
        npath = path.copy()
        npath.append(i)
        ipath = minpath(i, b, npath)
        if ipath[0] != -1: paths.append(ipath)
    if len(paths) == 0: return (-1, path)
    mpath = min(paths, key=lambda x: x[0])
    return (1+mpath[0], mpath[1])

mpath = minpath(a, b, [a])
if mpath[0] == -1: print('no route found')
else: print(*mpath[1])