# 치즈
import sys
from collections import deque

def bfs():
    visited = [[0] * M for _ in range(N)]
    
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    cnt = 0
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                
                if graph[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    
                elif graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
                    
    cheese.append(cnt)
    return cnt
                    

N, M = map(int, input().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

time = 0
cheese = []

while True:
    time += 1
    cnt = bfs()
    
    if cnt == 0:
        break
    
print(time-1)
print(cheese[-2])