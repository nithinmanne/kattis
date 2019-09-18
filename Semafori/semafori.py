N, L = map(int, input().split())
x, t = 0, 0
for _ in range(N):
    D, R, G = map(int, input().split())
    t += D - x
    x += D - x
    if t%(R+G) < R: t += R - t%(R+G)
print(t+L-x)