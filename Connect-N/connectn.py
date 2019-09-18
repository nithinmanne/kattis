X, Y, N = map(int, input().split())
grid = []
win = ''
for i in range(X):
    grid.append([])
    for j, val in enumerate(input().split()):
        grid[i].append({'R':0,'B':0, 'dir':'none'})
        if val != 'O':
            grid[i][j][val] = 1
            up, left, upleft, upright = 0, 0, 0, 0
            if i > 0: up = grid[i-1][j][val] if grid[i-1][j]['dir']=='up' or grid[i-1][j]['dir']=='none' else 0
            if j > 0: left = grid[i][j-1][val] if grid[i][j-1]['dir']=='left' or grid[i][j-1]['dir']=='none' else 0
            if i*j > 0: upleft = grid[i-1][j-1][val] if grid[i-1][j-1]['dir']=='upleft' or grid[i-1][j-1]['dir']=='none' else 0
            if i > 0 and j < Y-1: upright = grid[i-1][j+1][val] if grid[i-1][j+1]['dir']=='upright' or grid[i-1][j+1]['dir']=='none' else 0
            grid[i][j][val] += max(up, left, upleft, upright)
            if max(up, left, upleft, upright)==up: grid[i][j]['dir']='up'
            if max(up, left, upleft, upright)==left: grid[i][j]['dir']='left'
            if max(up, left, upleft, upright)==upleft: grid[i][j]['dir']='upleft'
            if max(up, left, upleft, upright)==upright: grid[i][j]['dir']='upright'
            if max(up, left, upleft, upright)==0: grid[i][j]['dir']='none'
            if grid[i][j][val] == N:
                win = {'B':'BLUE', 'R':'RED'}[val]
                break
    if win: break
if win: print(win, 'WINS')
else: print('NONE')