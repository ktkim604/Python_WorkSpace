# 숨바꼭질3
import sys
from collections import deque

def bfs(a):
    q = deque()
    q.append(a)

    while q:
        x = q.popleft()
        dx = [1,-1,x]
        
        if x == K:
            return visited[K]
        
        for i in range(3):
            
            nx = x + dx[i]
            
            if 0 <= nx < 100001 and visited[nx] == 0:
                if nx == x*2 and nx != 0:                      # 순간이동 하는 경우
                    visited[nx] = visited[x]    # 0초로 갱신 
                    q.appendleft(nx)            # 비용 0인 *2인 연산을 최우선적으로 처리하기위해
                    
                else:                           # 걸어서 이동하는 경우
                    visited[nx] = visited[x] + 1
                    q.append(nx)
                       

N, K = map(int, input().split())
visited = [0] * 100001

ans = bfs(N)
print(ans)

