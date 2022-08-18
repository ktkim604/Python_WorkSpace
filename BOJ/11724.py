from collections import deque
import sys

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                
    
    
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
    
visited = [False] * (n+1)

cnt = 0
for j in range(1, n+1):
    if not visited[j]:
        bfs(graph, j, visited)
        cnt += 1
print(cnt)
    

