# 빙산
import sys
from collections import deque
import copy
input = sys.stdin.readline

def check_area(a,b):
    q2 = deque()
    q2.append((a,b))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q2:
        x, y = q2.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx <= N and 0 <= ny <= M and graph[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q2.append((nx,ny))
    return visited

        
    
def bfs(v):

    q = deque(v)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    
    new_graph = copy.deepcopy(graph)

    while q:
        x, y = q.popleft()
        cnt = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= N and 0 <= ny <= M:
                if new_graph[nx][ny] == 0:
                    cnt += 1
        
        if cnt >= graph[x][y]:
            graph[x][y] = 0
        else:      
            graph[x][y] = graph[x][y] - cnt
        
    return graph
    

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

res = 0

while True:
    count = 0
    check_cnt = 0 
    v = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                v.append((i,j))
                count += 1


    visited = [[0]*M for _ in range(N)]
    bfs(v)
    temp = []
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                temp.append((i,j))
            
                
    for a,b in temp:
        if visited[a][b] == 0:
            visited[a][b] = 1
            check_area(a,b)
            check_cnt += 1
            
    if check_cnt >= 2:
        print(res+1)
        break            

    if count == 0:
        print(0)
        break
    
    res += 1

    

    

    