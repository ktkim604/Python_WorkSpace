# 단지번호붙이기
import sys
from collections import deque

def bfs(a,b):
    q = deque()
    q.append((a,b))
    graph[a][b] = 0
    cnt = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
                cnt += 1
                
    return cnt
        



n = int(input())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

home = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append(bfs(i,j))
            
home.sort()
print(len(home))
for k in home:
    print(k)
            

