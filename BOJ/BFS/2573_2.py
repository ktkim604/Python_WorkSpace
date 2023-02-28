# 빙산
import sys
from collections import deque

def bfs(a, b):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    q.append((a,b))
    visited[a][b] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx <= N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] != 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    
                else:
                    cnt[x][y] += 1
                    
    return 1

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
year = 0

while True:
    ans = []
    visited = [[0]*M for _ in range(N)]
    cnt = [[0]*M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and not visited[i][j]:
                ans.append(bfs(i,j))
                
    for i in range(N):
        for j in range(M):
            graph[i][j] -= cnt[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
    
    print(graph)
    
    if len(ans) == 0 or len(ans) >= 2:
        break
    
    year += 1
    
if len(ans) >= 2:
    print(year)
    
else:
    print(0)