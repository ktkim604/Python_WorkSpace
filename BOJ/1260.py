import sys
from collections import deque

n, m, start = map(int, sys.stdin.readline().split())


graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
    
def dfs(s):
    print(s, end = ' ')
    visited[s] = True
    for i in graph[s]:
        if not visited[i]:
            dfs(i)
            visited[i] = True

def bfs(s):
    queue = deque([s])
    visited[s] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
visited = [False] * (n+1)
dfs(start)
print()
visited = [False] * (n+1)
bfs(start)