# 게리맨더링
import sys
from collections import deque, defaultdict
from itertools import combinations

input = sys.stdin.readline

def bfs(group):
    q = deque()
    q.append(group[0])
    visit = [0] * (N+1)
    visit[group[0]] = 1

    while q:
        u = q.popleft()
        for v in graph[u]:
            if v in group and visit[v] == 0:
                q.append(v)
                visit[v] = 1
    for g in group:
        if visit[g] == 0:
            return False
        
    return True

N = int(input())
people = [0] + list(map(int, input().split()))

graph = defaultdict(list)

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    graph[i].extend(temp[1:])               # 그래프에 해당 노드 인접한 노드들 저장
    
print(graph)
V = [i for i in range(1, N+1)]
res = 9e9

for i in range(1, N//2+1):
    for g1 in combinations(V, i):
        g2 = []
        for j in V:
            if j not in g1:
                g2.append(j)
                
        if bfs(g1) and bfs(g2):
            g1_num = sum([people[g] for g in g1])
            g2_num = sum([people[g] for g in g2])
            
            res = min(res, abs(g1_num - g2_num))
            
if res == 9e9:
    print(-1)
else:
    print(res)    
            