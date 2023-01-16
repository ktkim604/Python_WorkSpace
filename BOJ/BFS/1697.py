# 숨바꼭질
import sys
from collections import deque

def bfs(s,c):
    q = deque()
    q.append((s,c))
    
    while q:
        x, cnt = q.popleft()
        dx = [-1,1,x]
        
        for i in range(3):
            nx = x + dx[i]
            
            if nx > 100000 or nx < 0:
                continue
            
            if visited[nx] == 0:        # Nx 방문을 안했다면
                q.append((nx, cnt+1))   # 큐에 해당 수 어펜드
                visited[nx] = cnt+1         # 해당 위치에 최소 도달 시간 입력
                
            elif visited[nx]:           # 방문을 했다면
                if cnt + 1 < visited[nx]:
                    visited[nx] = cnt + 1
                    q.append((nx, cnt+1))
    
    return visited[k]   # 동생있는 위치에 수빈이가 도달하는 최소 시간이 찍혀있음 
                
n, k = map(int, input().split())
visited = [0] * 100001
if n == k:
    print(0)
else:
    ans = bfs(n,0)
    print(ans)
