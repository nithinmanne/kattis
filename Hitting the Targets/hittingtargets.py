m = int(input())
rectangle = []
circle = []
for _ in range(m):
    shp, *p = input().split()
    if shp == 'rectangle': rectangle.append(list(map(int, p)))
    elif shp == 'circle': circle.append(list(map(int, p)))
    else: 1/0
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    h = 0
    for x1, y1, x2, y2 in rectangle:
        if x>=x1 and y>=y1 and x<=x2 and y<=y2: h += 1
    for xr, yr, r in circle:
        if (x-xr)**2+(y-yr)**2-r**2 <= 0: h += 1
    print(h)