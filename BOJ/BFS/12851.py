# 숨바꼭질 2

import sys
from collections import deque

def bfs():
    q = deque()
    q.append((N,0))
    temp = []
    
    while q:
        x, cnt = q.popleft()
        dx = [-1,1,x]
        
        if x == K:
            temp.append(cnt)
        
        for i in range(3):
            nx = x + dx[i]
            
            if 0 <= nx < 100001:
                if visited[nx] == 0:
                    q.append((nx, cnt+1))
                    visited[nx] = cnt+1
                    
                elif visited[nx]:
                    if visited[nx] >= cnt+1:
                        q.append((nx, cnt+1))
                        visited[nx] = cnt+1
                        
    return temp
                                           
N, K = map(int, input().split())

visited = [0] * 100001
count = 0

ans = bfs()
min_value = min(ans)

if N == K:
    print(0)
    print(1)
    
else:
    for i in ans:
        if i == min_value:
            count += 1
            
    print(min_value)
    print(count)
