# 토마토
import sys
from collections import deque
import copy

def bfs():
    if not q:
        return -1
    
    while q:
        x, y, cnt = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx,ny,cnt+1))
    
    return cnt
    

m, n = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]
    
q = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j,0))
            

ans = bfs()

for num in graph:
    for k in num:
        if k == 0:
            print(-1)
            exit(0)
        
print(ans)  

