from collections import deque
from contextlib import AsyncExitStack
import sys


def bfs(x, y):
    q = deque()
    q.append((0, x, y))
    visited[x][y] = 1
    
    
    while q:
        cnt, x, y = q.popleft()
        if x == end_x and y == end_y:
            print(cnt)
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if not visited[nx][ny]:
                    
                    visited[nx][ny] = 1
                    q.append((cnt+1, nx, ny))
                    
    
        


t = int(input())
for _ in range(t):
    l = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    
    visited = [ [0] * l for _ in range(l)]
    dx = [2,2,1,-1,-2,-2,-1,1]
    dy = [1,-1,2,2,1,-1,-2,-2]    
    bfs(start_x, start_y)
   