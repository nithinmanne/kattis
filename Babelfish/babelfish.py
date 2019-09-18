from sys import stdin
from collections import defaultdict as ddict
dic = True
mapp = ddict(lambda:'eh')
for i in stdin:
    if dic:
        j=i.split()
        if len(j)==0:
            dic=False
            continue
        mapp[j[1]]=j[0]
    else:
        print(mapp[i.strip()])