from collections import deque
import sys


def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 2
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0: 
                q.append((nx, ny))
                graph[nx][ny] = 2
                
    
    
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
#찾는 방향 설정
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 0으로 시작하는 부분 출발 지점
for j in range(m):
    if graph[0][j] == 0:
        bfs(0,j)
        
if 2 in graph[-1]:
    print("YES")
else:
    print("NO")
        
        

