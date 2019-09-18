def gcd(a, b): return a if a==b else gcd(a-b,b) if a>b else gcd(a,b-a)
print(gcd(*map(int, input().split())))