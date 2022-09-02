from collections import deque
import sys

def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = 1
    cnt = 0
    while q:
        com = q.popleft()
        for i in graph[com]:
            if visited[i] == 0:
                cnt += 1
                q.append(i)
                visited[i] = 1
                
    return cnt

n = int(input())
m = int(input())
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
ans = bfs(1)
print(ans)
