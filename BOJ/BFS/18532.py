# 특정 거리의 도시 찾기
import sys
from collections import deque

def bfs(s, cnt):
    q = deque()
    q.append((s, cnt))
    visited[s] = True
    
    num_list = []
    
    while q:
        v, c = q.popleft()
        if c == k:
            num_list.append(v)
        
        for i in graph[v]:
            if visited[i]==False:
                visited[i] = True
                q.append((i, c+1))
                
    num_list.sort()
    for j in num_list:
        print(j)
        
    if len(num_list) == 0:
        print(-1)

n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    
    
bfs(x, 0)
