# 점프 점프
import sys
from collections import deque

def bfs(s, j):
    q = deque([(s, j)])
    
    while q:
        pos, jump = q.popleft()
        for i in range(1, jump+1):
            if pos+i >= n or visited[pos+i]:
                continue
            visited[pos+i] = visited[pos] + 1 
            q.append((pos+i, arr[pos+i]))
    if visited[-1]:
        print(visited[-1])
    else:
        print(-1)

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
visited = [0] * n

if n == 1:
    print(0)
else:
    bfs(0, arr[0])
