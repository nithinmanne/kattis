def M(n): return n-10 if n>100 else M(M(n+11))
print(M(int(input())))