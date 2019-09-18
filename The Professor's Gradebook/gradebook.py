from math import ceil

N, M = map(int, input().strip().split())
name = []
st = []
sg = []

for i in range(N):
    inp = input().strip().split()
    name.append(inp[0])
    sti = list(map(int, inp[1:]))
    st.append(sum(sti) - min(sti[:-1]))

mx = max(st)

for i in range(N):
    sgi = ceil(100.*st[i]/mx)
    sg.append(sgi)
    if sgi >= 90: g = 'A'
    elif sgi >= 80: g = 'B'
    elif sgi >= 70: g = 'C'
    elif sgi >= 60: g = 'D'
    else: g = 'F'
    
    print(name[i], st[i], sg[i], g)