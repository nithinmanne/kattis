for _ in range(int(input())):
    inp = input().lower()
    cha = list('abcdefghijklmnopqrstuvwxyz')
    for i in inp:
        if i in cha: cha.remove(i)
    if len(cha)==0: print('pangram')
    else: print('missing', ''.join(cha))