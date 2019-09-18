import sys
f = sys.stdin
N, M, S, R = map(int, f.readline().strip().split())
ships = []
for _ in range(S): ships.append(tuple(map(int, f.readline().strip().split())))
score = 0
for _ in range(R):
    x, y = map(int, f.readline().strip().split())
    mind = float('inf')
    for ship in ships:
        dis = abs(ship[0]-x)+abs(ship[1]-y)
        if dis < mind:
            mind = dis
            mins = ship
        if mind == 0: break
    score += max(0, 1000 - mind*100)
    if mind == 0:
        ships.remove(mins)
    if len(ships)==0: break
print '{}/{} ships sunk. Score: {} points'.format(S-len(ships), S, score)
