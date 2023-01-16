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
            if 0 < nx < 100001:
                if visited[nx] == 0:            # 수빈이가 방문안한 위치라면
                    visited[nx] = cnt + 1
                    q.append((nx, cnt+1))
                    
                elif visited[nx]:               # 수빈이가 방문했던 위치라면
                    if cnt + 1 < visited[nx]:   # 기존에 있던 도달 횟수보다 새로 들어온 값이 더 작다면
                        visited[nx] = cnt + 1   # 도달 횟수 갱신
                        q.append((nx, cnt + 1)) # 추가적으로 계속 탐색
            
    return visited[k]


n, k = map(int, input().split())
visited = [0] * 100001
if n == k:
    print(0)
else:      
    ans = bfs(n, 0)
    print(ans)