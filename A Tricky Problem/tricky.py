N = int(input())
scoremap = { '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'J':10, 'Q':11, 'K':12, 'A':13 }
p1 = list(map(lambda x: scoremap[x], input().split()))
p2 = list(map(lambda x: scoremap[x], input().split()))
p1s, p2s = 0, 0
for i in range(N):
    if p1[i] > p2[i]: p1s += 1
    elif p1[i] < p2[i]: p2s += 1
if p1s > p2s: print('PLAYER 1 WINS')
elif p1s < p2s: print('PLAYER 2 WINS')
else: print('TIE')