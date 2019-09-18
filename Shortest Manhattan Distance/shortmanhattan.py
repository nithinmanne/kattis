def pathprint(p0,p1,dl,path):
    if dl==0 and p0!=p1: return
    elif p0==p1:
        print(*path)
        return
    if p0[0]>p1[0]:
        lpath=path.copy()
        lpath.append('left')
        pathprint((p0[0]-1,p0[1]),p1,dl-1,lpath)
    elif p0[0]<p1[0]:
        rpath=path.copy()
        rpath.append('right')
        pathprint((p0[0]+1,p0[1]),p1,dl-1,rpath)
    if p0[1]<p1[1]:
        upath=path.copy()
        upath.append('up')
        pathprint((p0[0],p0[1]+1),p1,dl-1,upath)
    elif p0[1]>p1[1]:
        dpath=path.copy()
        dpath.append('down')
        pathprint((p0[0],p0[1]-1),p1,dl-1,dpath)

x0, y0, x1, y1 = map(int, input().split())
dis = abs(x0-x1) + abs(y0-y1)
path = []
if dis==0: print('NONE')
else: pathprint((x0,y0),(x1,y1),dis,[])