while True:
    n, *k = map(int, input().split())
    if n==0: break
    inp = input()
    if len(inp)%n != 0:
        inp += ' '*(n-len(inp)%n)
    out = []
    for i in range(len(inp)//n):
        for j in k:
            out.append(inp[i*n:i*n+n][j-1])
    print("'", *out, "'", sep='')