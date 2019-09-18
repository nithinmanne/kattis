from collections import defaultdict as ddict

L, N, k, Q = map(int, input().strip().split())
s = ''
for _ in range(L): s += input()

kmers = ddict(lambda:0)

for i in range(N-k+1):
    kmers[s[i:i+k]] += 1

for _ in range(Q):
    kmer = input()
    print(kmer, kmers[kmer])