from collections import deque
import sys

def bfs(start):
    q = deque()
    q.append((0, start))
    visited[start] = 1
    
    while q:
        cnt, v = q.popleft()
        
        if v == b:
            return cnt

        for i in graph[v]:
            if not visited[i]:
                visited[i] = 1
                q.append((cnt+1,i))
            
    if v != b:
        return -1
        

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)


for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
ans = bfs(a)
print(ans)
    