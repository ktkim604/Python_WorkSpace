# 벽 부수고 이동하기 2
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((0,0,1,K))
    visited[0][0][K] = 1
    
    while q:
        x,y,cnt,crash = q.popleft()
        
        if x == N-1 and y == M-1:
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][crash]:
                if crash and graph[nx][ny] == 1:
                    q.append((nx,ny,cnt+1,crash-1))
                    visited[nx][ny][crash-1] = 1
                    
                elif graph[nx][ny] == 0:
                    q.append((nx,ny,cnt+1,crash))
                    visited[nx][ny][crash] = 1
                    
    return -1
                    
    
    

N, M, K = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = bfs()

print(ans)



