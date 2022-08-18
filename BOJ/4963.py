import sys
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    dx = [-1,1,0,0,1,1,-1,-1]
    dy = [0,0,-1,1,1,-1,1,-1]
    
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
    
    visited = [ [0] * w for _ in range(h)]
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                cnt += 1
    
    print(cnt)
    
    
    