if int(input()): print(len(list(filter(lambda x: x<0, map(int, input().split())))))
else: print(0)