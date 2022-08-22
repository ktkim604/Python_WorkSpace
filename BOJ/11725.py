from collections import deque
import sys

#Bfs 너비 탐색 
def bfs(start):
    q = deque()
    q.append(start)
    
    while q:
        v = q.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                visited[i] = v
                q.append(i)
    

# 그래프 만들기
n = int(input())
graph = [ [] for i in range(n+1)]

for i in range(1, n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 처리를 위한 리스트 생성
visited = [0] * (n+1)
bfs(1)

# 2번째 노드부터 체크 
for i in range(2, n+1):
    print(visited[i])
    
