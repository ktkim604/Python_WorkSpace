# 스타트링크
import sys
from collections import deque

def bfs(a, c):
    q = deque()
    q.append((a,c))
    visited[a] = 1

    while q:
        y, cnt = q.popleft()
        
        for i in range(2):
            ny = y +dy[i]
            if 0 < ny <= F and not visited[ny]:     # 방문리스트에 누른 버튼의 수 저장
                q.append((ny, cnt+1))
                visited[ny] = cnt+1
            elif 0 < ny <= F and visited[ny]:
                if visited[ny] > cnt+1:
                    q.append((ny, cnt+1))
                    visited[ny] = cnt+1
                    
    return visited[G]
                
        

F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)
dy = [U, -D]

ans = bfs(S, 0)

if ans == 0:
    print('use the stairs')
    
else:
    print(ans)