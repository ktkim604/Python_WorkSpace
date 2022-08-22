from collections import deque
import sys

def bfs(start):
    q = deque()
    q.append(start)
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = v
                q.append(i)

n = int(input())
graph = [ [] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0] * (n+1)
bfs(1)

for i in range(2,n+1):
    print(visited[i])
