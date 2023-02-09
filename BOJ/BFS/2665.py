# 미로만들기
import sys
from collections import deque

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 0
    
    while q:
        x,y = q.popleft()
        
        if x == N-1 and y == N-1:
            return visited[N-1][N-1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if graph[nx][ny] == 1:                  # 흰방이라면 검은방으로 바꾸지 않았으므로 이전값 유지
                    visited[nx][ny] = visited[x][y]     
                    q.appendleft((nx,ny))
                    
                else:                                   # 검은방이라면 바꿀때마다의 횟수를 늘려가며 저장
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))


N = int(input())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

visited = [[-1] * N for _ in range(N)]           # 검은방으로 바꿀때마다 횟수를 저장시킴

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = bfs()
print(ans)