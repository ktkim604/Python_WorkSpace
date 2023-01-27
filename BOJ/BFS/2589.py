# 보물섬
import sys
from collections import deque

def bfs(a,b,c):
    q = deque()
    q.append((a,b,c))
    visited[a][b] = 1
    
    while q:
        x, y, cnt = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 'L':
                visited[nx][ny] = 1
                q.append((nx,ny,cnt+1))
    
    return cnt
    
    

n, m = map(int, input().split())
graph = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = []

for i in range(n):
    for j in range(m):
        visited = [[0] * m for _ in range(n)]
        if graph[i][j] == 'L':
            ans.append(bfs(i,j,0))
            
print(max(ans))

            