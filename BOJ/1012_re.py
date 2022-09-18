import sys
from collections import deque


def bfs(x,y):
    q = deque()
    q.append((x,y))
    
    while q:
        v = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1: 
                q.append((nx, ny))
                graph[nx][ny] = 2
                
    return 1
        
    
    
    
t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for i in range(n)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    for j in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
    cnt = 0
    
    for i in range(n):
        for j in range(m):
            cnt += bfs()
    
    print(cnt)  

        
        
    