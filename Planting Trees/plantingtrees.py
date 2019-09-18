input()
inp = []
for i, j in enumerate(sorted(map(int, input().split()), reverse=True)):
    inp.append(i+j+1)
print(1+max(inp))