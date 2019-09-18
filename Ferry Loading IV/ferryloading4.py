for _ in range(int(input())):
    l, m = map(int, input().split())
    l *= 100
    cars = { 'left': [], 'right':[] }
    for _ in range(m):
        cl, cpos = input().split()
        cars[cpos].append(int(cl))

    posl = [ 'left', 'right' ]
    fpos = 0
    rcrst = 0
    while(len(cars['left'])+len(cars['right']) > 0):
        if len(cars[posl[fpos]]) == 0:
            fpos = 1 - fpos
            rcrst += 1
        flnus = 0
        ncars = 0
        lncars = len(cars[posl[fpos]])
        while flnus + cars[posl[fpos]][ncars] < l:
            flnus += cars[posl[fpos]][ncars]
            ncars += 1
            if ncars == lncars: break
        cars[posl[fpos]] = cars[posl[fpos]][ncars:]
        fpos = 1 - fpos
        rcrst += 1
    
    print(rcrst)