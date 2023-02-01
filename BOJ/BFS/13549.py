# 숨바꼭질3
import sys
from collections import deque

def bfs(a):
    q = deque()
    q.append(a)

    while q:
        x = q.popleft()
        
        if x == K:
            return visited[K]
        
        for next in (x-1, x+1, x*2):
            if 0 <= next < 100001 and visited[next] == 0:
                if next == x*2:                      # 순간이동 하는 경우
                    visited[next] = visited[x]    # 0초로 갱신 
                    q.appendleft(next)            # 비용 0인 *2인 연산을 최우선적으로 처리하기위해
                    
                else:                           # 걸어서 이동하는 경우
                    visited[next] = visited[x] + 1
                    q.append(next)
                        
                        

N, K = map(int, input().split())
visited = [0] * 100001

ans = bfs(N)
print(ans)

