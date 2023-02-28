# 트리의 지름
import sys
from collections import deque

input = sys.stdin.readline

def bfs(s,c):
    visited = [0] * (N+1)
    q = deque()
    q.append((s,c))
    visited[s] = 1
    max_value = 0
    ans = []
    
    while q:
        v, cnt = q.popleft()
        ans.append((v, cnt))
        
        for j in graph[v]:
            if not visited[j[0]]:
                q.append((j[0], cnt + j[1]))
                visited[j[0]] = 1
                
        
    temp = sorted(ans, key = lambda x : -x[1])    

    return temp[0][0], temp[0][1]
                

N = int(input())
graph = [[] for _ in range(N+1)]

for i in range(N-1):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
start, count1 = bfs(1,0)
last, count2 = bfs(start, 0)
print(count2)