# 토마토
import sys
from collections import deque

def bfs():
    if not q:
        return -1
    
    while q:
        z,x,y,cnt = q.popleft()
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and graph[nz][nx][ny] == 0:
                print(nz,nx,ny)
                graph[nz][nx][ny] = 1
                q.append((nz,nx,ny,cnt+1))
                     
    return cnt              

m, n, h = map(int, input().split())
q = deque([])

graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]


for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i,j,k,0))
       
     
                
ans = bfs() 



print(graph)


for num in graph:
    print(num)
    for number in num:
        print(number)
        for N in number:
            if N == 0:
                print(-1)
                exit(0)
      
print(ans)
