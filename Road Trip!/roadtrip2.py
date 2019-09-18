N, R, H, M, S = map(int, input().split())
city = []
road = []
for _ in range(N):
    _, s, t = input().split()
    city.append([s, int(t), -H])
    road.append([M]*N)
for _ in range(R):
    f, t, d = map(int, input().split())
    road[f][t] = road[t][f] = d
T = city[S][1]
s = [S]
while T < M:
    city[s[-1]][2] = T
    pos = []
    for i,j in enumerate(road[s[-1]]):
        if T+j-city[i][2]>=H and T+j+city[i][1]<=M:
            pos.append((i,j))
    if not pos: break
    ns = min(pos, key=lambda x:x[1])
    T += ns[1]+city[ns[0]][1]
    s.append(ns[0])
print(*map(lambda x: city[x][0], s))
print(T)

    