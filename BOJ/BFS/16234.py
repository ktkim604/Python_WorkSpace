# 인구이동
import sys
from collections import deque

def bfs(a,b):
    P = []
    q = deque()
    q.append((a,b))
    P.append((a,b))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(A[x][y]-A[nx][ny]) <= R:    # 국경선을 공유하는 두나라의 차이가 L 이상 R 이하라면
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    P.append((nx,ny))                   # 공유하고 있는 나라의 좌표를 P리스트에 추가 
                    
    return P
                    
                    
N, L, R = map(int, input().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0
while True:
    
    visited = [[0] * (N) for _ in range(N)]
    flag = 0
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                ans = bfs(i,j)

                
                if len(ans) > 1:
                    flag = 1
                    num = sum([(A[x][y]) for x,y in ans]) // len(ans)
                    for x,y in ans:
                        A[x][y] = num
    if flag == 0:
        break
    
    cnt += 1 
              
print(cnt)

    