#결혼식
from collections import deque
import sys

def bfs(node):
    q = deque()
    q.append((0, node))
    visited[node] = 1
    
    while q:
        cnt, v = q.popleft()
        if cnt == 2:
            continue
        for i in graph[v]:
            if visited[i] == 0:
                q.append((cnt+1, i))
                visited[i] = 1
                
        
    
    
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0] * (n+1)

bfs(1)
print(visited.count(1)-1)