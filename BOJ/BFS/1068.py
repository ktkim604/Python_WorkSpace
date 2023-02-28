# 트리
import sys
from collections import deque

def bfs(r):
    q = deque()
    q.append(r)
    cnt = 0                         # 리프 노드 갯수를 세기위한 변수 0으로 설정
    
    while q:
        x = q.popleft()        
        print(x)     
        
        if visited[x] == 1:         # 삭제된 노드라면 
            continue
        if len(tree[x]) == 0:       # 해당 노드에 자식들이 없다면 (리프 노드라면)
            cnt += 1
            continue
        
        n = len(tree[x])            # 해당 노드에 묶여있는 자식들의 갯수를 n으로 저장
        
        while tree[x]:              # 묶여있는 자식 노드들이 없어질 때 까지
            y = tree[x].pop()       # 자식 노드들 하나씩 꺼내서 변수 y에 저장
            if n == 1 and visited[y] == 1:  # 묶여있는 자식노드들의 총 갯수가 한개이고 그놈이 삭제된 노드라면
                cnt += 1            # 자식위에 부모노드가 일반 리프노드로 바뀌므로 리프노드 카운트 1개 추가
                break               # 그리고 해당 반복문 빠져나감
            else:                   # 그게 아니면
                q.append(y)         # 큐에 해당 노드 어펜드
        
    return cnt
            

n = int(input())
node = list(map(int, input().split()))
delete = int(input())

visited = [0 for _ in range(n)]         # 지운 노드 표시하기 위함
tree = [[] for _ in range(n)]      # 같은 부모노드에 엮여있는 노드끼리 묶어줌

visited[delete] = 1                     # 지울 노드 번호 1로 표시

# 부모 노드가 없다면 그 녀석을 루트로 지정하고 아니면 같은 부모를 가지는 녀석들끼리 묶어서 트리큐에 넣어줌
for i in range(n):
    if node[i] == -1:
        root = i

    else:
        tree[node[i]].append(i)
        
ans = bfs(root)                         # 루트부터 탐색 시작
print(ans)
