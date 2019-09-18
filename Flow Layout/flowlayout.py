m = int(input())
while m:
    mw, cw = 0, 0
    oh, ch = 0, 0
    w, h = map(int, input().split())
    while w != -1 and h != -1:
        if cw + w > m:
            cw = w
            oh += ch
            ch = h
        else:
            cw += w
            if h > ch: ch = h
        if cw > mw: mw = cw
        
        w, h = map(int, input().split())
    
    oh += ch
    
    print(f'{mw} x {oh}')
    
    m = int(input())