# 안전 영역
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
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny))
                

n = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt_lst = []
min_val = 1

for k in range(0, 101):
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= k:
                visited[i][j] = 1

    cnt = 0
    for l in range(n):
        for m in range(n):
            if visited[l][m] == 0:
                bfs(l,m)
                cnt += 1 
    cnt_lst.append(cnt)

print(max(min_val, max(cnt_lst)))
