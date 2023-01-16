# 맥주 마시면서 걸어가기
import sys
from collections import deque

def bfs(a,b):
    q = deque()
    q.append((a,b))
    
    while q:
        x, y = q.popleft()
        
        if abs(festival[0] - x) + abs(festival[1] - y) <= 1000:
            return 'happy'
            
        for i in range(n):
            if not visited[i]:
                GS_x, GS_y = GS[i]
                if abs(GS_x - x) + abs(GS_y - y) <= 1000:
                    q.append((GS_x, GS_y))
                    visited[i] = 1
    
    return 'sad'

    

t = int(input())
for _ in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    GS = []
    for i in range(n):
        x, y = map(int, input().split())
        GS.append((x,y))
    festival = list(map(int, input().split()))
    
    visited = [0 for _ in range(n+1)]
    
    ans = bfs(home[0], home[1])
    print(ans)
    
    