commname = input()
n = int(input())
p, h, r, c = 0, 0, 0, 0
for _ in range(n):
    nam = input()
    if commname == nam[:len(commname)]: p+=1
    elif commname == nam[-len(commname):]: h+=1
    elif commname in nam: r+=1
    else: c+=1
print('{} PRINCESS'.format(p))
print('{} BARON'.format(h))
print('{} PRIEST'.format(r))
print('{} COMMONER'.format(c))