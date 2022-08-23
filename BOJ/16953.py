from collections import deque
import sys

def bfs(node):
    q = deque()
    q.append((1, node))
    
    while q:
        cnt, v = q.popleft()
        if v > b:
            continue
        if v == b:
            return cnt
        q.append((cnt+1, int(str(v)+'1')))
        q.append((cnt+1, v * 2))
        
    if v != b:
        return -1



a, b = map(int, input().split())

ans = bfs(a)
print(ans)