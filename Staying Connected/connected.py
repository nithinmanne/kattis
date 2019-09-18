from collections import defaultdict as ddict
V = int(input())
E = int(input())

edges = ddict(lambda: set())
for _ in range(E):
    x, y = map(int, input().split())
    edges[x].add(y)
    edges[y].add(x)
visited = [False]*V
graph = (edges, visited)

def dfs(graph, root_vertex):
    graph[1][root_vertex] = True
    for vertex in graph[0][root_vertex]:
        if not graph[1][vertex]: dfs(graph, vertex)

conn = 0
while(not all(visited)):
    conn += 1
    dfs(graph, visited.index(False))

print(conn)
    