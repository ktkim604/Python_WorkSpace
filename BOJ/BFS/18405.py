# 경쟁적 전염
import sys
from collections import deque

def bfs():
    
    while dq2:
        x,y,d,cnt = dq2.popleft()
        
        if cnt == s:
            return graph[a-1][b-1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]
                dq2.append((nx,ny,0,cnt+1))
        
    return graph[a-1][b-1]

n, k = map(int, input().split())        # nxn 표, 1~k까지 바이러스 종류
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
s,a,b = map(int, input().split())       # s초 후에 (x,y)에 있는 바이러스 종류

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque([])

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            q.append((i,j,graph[i][j],0))

dq2 = deque(sorted(q, key = lambda x : x[2]))

ans = bfs()
print(ans)



