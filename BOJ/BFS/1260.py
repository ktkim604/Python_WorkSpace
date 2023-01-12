import sys
from collections import deque

n, m, start = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
    
def bfs(s):
    q = deque([s])
    visited[s] = True
    
    while q:
        v = q.popleft()
        print(v, end=' ')
        for j in graph[v]:
            if not visited[j]:
                q.append(j)
                visited[j] = True
                
bfs(start)
