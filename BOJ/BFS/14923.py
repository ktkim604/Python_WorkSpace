# 미로 탈출
import sys
from collections import deque

def bfs():
    q = deque()
    q.append((Hx-1,Hy-1,0,1))
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[Hx-1][Hy-1][1] = 1
    
    while q:
        x, y, cnt, magic = q.popleft()
        
        if x == Ex-1 and y == Ey-1:
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][magic] == 0:
                
                if magic == 1 and graph[nx][ny] == 1:           # 지팡이가 있고 벽을 만났을때
                    visited[nx][ny][1] = 1                      # 벽을 부수면서(즉, 지팡이 하나를 쓰면서) 방문처리
                    q.append((nx,ny,cnt+1,magic-1))             # 거리 1 추가하면서 지팡이 하나 쓴값을 제거해주고 다시 어팬드
                
                elif graph[nx][ny] == 0:                        # 
                    visited[nx][ny][magic] = 1
                    q.append((nx,ny,cnt+1,magic))
                
    return -1


N,M = map(int, input().split())
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = bfs()
print(ans)

