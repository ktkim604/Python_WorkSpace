# 벽 부수고 이동하기
import sys
from collections import deque

def bfs():
    q = deque()
    q.append((0,0,1,0))
    visited[0][0][1] = 1
    
    while q:
        x,y,crash,cnt = q.popleft()
        
        if x == N-1 and y == M-1:
            return cnt + 1
            
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][crash]:
                if crash == 1 and graph[nx][ny] == 1:
                    visited[nx][ny][0] = 1
                    q.append((nx,ny,0,cnt+1))
                    
                    
                elif graph[nx][ny] == 0:
                    visited[nx][ny][crash] = 1
                    q.append((nx,ny,crash,cnt+1))
                    
    return -1
                    

N, M = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs())



