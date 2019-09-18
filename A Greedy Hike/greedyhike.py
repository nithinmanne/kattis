X, Y = map(int, input().strip().split())
xs, ys = map(int, input().strip().split())
m = []
for _ in range(X):
    m.append(list(map(int, input().strip().split())))
x = xs
s = 0
for y in range(ys, Y-1):
    if x!=0 and x!=X-1:
        mine = min(abs(m[x][y+1]-m[x][y]), abs(m[x+1][y+1]-m[x][y]), abs(m[x-1][y+1]-m[x][y]))
        if abs(m[x][y+1]-m[x][y]) == mine: x = x
        elif abs(m[x+1][y+1]-m[x][y]) == mine: x = x+1
        else: x = x-1
    elif x!=X-1:
        mine = min(abs(m[x][y+1]-m[x][y]), abs(m[x+1][y+1]-m[x][y]))
        if abs(m[x][y+1]-m[x][y]) == mine: x = x
        else: x = x+1
    elif x!=0:
        mine = min(abs(m[x][y+1]-m[x][y]), abs(m[x-1][y+1]-m[x][y]))
        if abs(m[x][y+1]-m[x][y]) == mine: x = x
        else: x = x-1
    else:
        mine = abs(m[x][y+1]-m[x][y])
    s += mine
print(x, Y-1, s)