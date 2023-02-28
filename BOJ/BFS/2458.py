# 키 순서
# 플로이드-와샬 알고리즘을 사용
# 특정 노드가 다른 노드를 가리키는 횟수 + 다른 노드가 특정 노드를 가리키는 횟수 == N-1 이라면
# 그 특정 노드의 순서를 알 수 있다는 점이 핵심

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] * N for _ in range(N)]


for _ in range(M):
    s, t = map(int, input().split())
    graph[s-1][t-1] = 1


# 플로이드-와샬 알고리즘 이용, 임의의 숫자 i, j에 대해 연결되어 있는지를 검사
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

ans = 0
for i in range(N):
    check = 0
    for j in range(N):
        check += graph[i][j] + graph[j][i]
    
    if check == (N-1):
        ans += 1
        
print(ans)
    
