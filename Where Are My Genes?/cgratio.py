N = int(input().strip())

c, g, a, t = 0, 0, 0, 0

for _ in range(N):
    i = input()
    c += i.count('C')
    g += i.count('G')
    a += i.count('A')
    t += i.count('T')
    
print(100.*(c+g)/(c+g+a+t))