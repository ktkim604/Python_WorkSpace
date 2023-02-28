# 적록 색약
import sys
from collections import deque

def bfs(a,b):
    q = deque()
    q.append((a,b))
    visited[a][b] = 1
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[x][y] == graph[nx]:
                q.append((nx,ny))
                visited[nx][ny] = 1
                
                
n = int(input())
graph = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt1, cnt2 = 0, 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt1 += 1

visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j]=='R':
            graph[i][j]='G'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt2 += 1
            
print(cnt1, cnt2)