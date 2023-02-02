# 뱀과 사다리
import sys
from collections import deque

def bfs():
    q = deque()
    q.append((1,0))
    
    while q:
        x, cnt = q.popleft()
        
        if x == 100:
            return cnt
        
        for dice in range(1, 7):
            nx = x + dice
            if nx <= 100 and not visited[nx]:
                if nx in ladders.keys():
                    nx = ladders[nx]
                    visited[nx] = 1
                    q.append((nx,cnt+1))
                    
                if nx in snakes.keys():
                    nx = snakes[nx]
                    visited[nx] = 1
                    q.append((nx,cnt+1))
                    
                if not visited[nx]:
                    visited[nx] = 1
                    q.append((nx,cnt+1))
                

N,M = map(int, input().split())
graph = [0] * 101
visited = [0] * 101

ladders = dict()
snakes = dict()

for _ in range(N):
    i, j = map(int, input().split())
    ladders[i] = j
    
for _ in range(M):
    i, j = map(int, input().split())
    snakes[i] = j
    
print(bfs())
    


