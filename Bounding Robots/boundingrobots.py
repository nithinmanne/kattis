w, l = map(int, input().split())
while w!=0 and l!=0:
    n = int(input())
    ax, ay, cx, cy = 0, 0, 0, 0
    for _ in range(n):
        d, le = input().split()
        le = int(le)
        if d=='u':
            cy += le
            if ay+le<l: ay += le
            else: ay = l-1
        if d=='d':
            cy -= le
            if ay-le>=0: ay -= le
            else: ay = 0
        if d=='r':
            cx += le
            if ax+le<w: ax += le
            else: ax = w-1
        if d=='l':
            cx -= le
            if ax-le>=0: ax -= le
            else: ax = 0
    print(f'Robot thinks {cx} {cy}')
    print(f'Actually at {ax} {ay}\n')
    w, l = map(int, input().split())