import sys
from collections import deque

def bfs(a,b):
    q = deque()
    q.append((a,b))
    graph[a][b] = 1
    cnt = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                q.append((nx,ny))
                graph[nx][ny] = 1
                cnt += 1
                
    return cnt


m, n, k = map(int, input().split())
graph = [[0]*n for i in range(m)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]


for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

res = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            res.append(bfs(i,j))
res.sort()

print(len(res))
for r in res:
    if r == res[-1]:
        print(r)
    else:
        print(r, end=' ')