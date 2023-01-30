# 트리
import sys
from collections import deque

def bfs(r):
    q = deque()
    q.append(r)
    cnt = 0
    while q:
        x = q.popleft()
        if visited[x] == 1:
            continue
        if len(tree[x]) == 0:
            cnt += 1
            continue
        
        n = len(tree[x])
        
        while tree[x]:
            y = tree[x].pop()
            if n == 1 and visited[y] == 1:
                cnt += 1
                break
            else:
                q.append(y)
        
    return cnt
            
            
n = int(input())
node = list(map(int, input().split()))
delete = int(input())

visited = [0 for _ in range(n)]
tree = deque([] for _ in range(n))

visited[delete] = 1

for i in range(n):
    if node[i] == -1:
        root = i

    else:
        tree[node[i]].append(i)
        
ans = bfs(root)
print(ans)
