n, V = map(int, input().split())
v = []
for _ in range(n):
    l, w, h = map(int, input().split())
    v.append(l*w*h)
print(max(v)-V)