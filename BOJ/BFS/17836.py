# 공주님을 구해라 !
import sys
from collections import deque

def bfs(a,b,c):
    global answer
    q = deque()
    q.append((a,b,c))
    visited[a][b] = 1
    
    while q:
        x,y,cnt = q.popleft()

        if graph[x][y] == 2:
            answer = cnt + (N-1-x) + (M-1-y)
        
        if x == N-1 and y == M-1:
            return min(cnt, answer)
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] != 1:
                q.append((nx,ny,cnt+1))
                visited[nx][ny] = 1
                
    return answer
        
    
N, M, T = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer = 10001
ans = bfs(0,0,0)

if ans > T: 
    print('Fail')
    
else:
    print(ans)