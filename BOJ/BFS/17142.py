# 연구소 3
import sys
from collections import deque
import itertools
import copy

input = sys.stdin.readline

def find_max(new_graph):
    max_time = -1                                       # 최대값을 비교하기 위해 음수로 초기값 설정
    for i in range(N):
        for j in range(N):
            if new_graph[i][j] == 0:                    # 그래프를 찾다가 0 이 있으면 큰수 리턴
                return int(1e9)
            # if new_graph[i][j] == '*':                  # 비활성 -> 활성 안된 놈도 큰수 리턴
            #     return int(1e9)
            if type(new_graph[i][j]) is int:            # 그래프 좌표를 하나씩 돌며 그놈의 타입이 int형이라면
                max_time = max(max_time, new_graph[i][j])    # 바이러스가 다 번진 경우 그 그래프에 해당하는 최대값을 찾아냄
    return max_time                                     # 해당 max_time 리턴


def bfs(v):
    global graph
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque(v)
    new_graph = [[*g] for g in graph]           # deepcopy 와 같은 구조 (그래프 원본 유지)
    
    cnt = 1
    for a, b in v:
        new_graph[a][b] = cnt                   # 경우의수로 올라온 활성 바이러스 놈들을 1로 지정
    
    for i in range(N):              
        for j in range(N):
            if new_graph[i][j] == 2:            # 활성으로 바꾸고 남은 바이러스를 찾아서
                new_graph[i][j] = "*"           # '*' 로 바꿔서 표기
                
    # while 문 두개 사용하고 q를 두개 사용
    while True:        
        q2 = deque()                            # 큰 무한루프 안에서 cnt를 반복적으로 갱신해주기 위해 q2 생성                          
        cnt += 1                                # 큐에 담겨있는 놈들 탐색하면서 뻗어나갈때마다 1씩 증가시킴
        while q:
            x, y = q.popleft()                  
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < N and new_graph[nx][ny] != "-":
                    if new_graph[nx][ny] == 0:  
                        q2.append([nx, ny])             # 바로 q에 어팬드 시켜버리면 작은 무한루프 안빠져 나가므로 q2에 어팬드
                        new_graph[nx][ny] = cnt
                    elif new_graph[nx][ny] == "*":      # 비활성 바이러스 만나면
                        new_graph[nx][ny] = "**"        # 활성 바이러스로 바꿔주는 표시 '**'
                        q2.append([nx, ny])             
        for elem in q2:                                 # q에 담긴 놈들 다 빠지고 작은 무한루프 탈출시에 다시 q에 탐색 요소들 어팬드
            q.append(elem)
        if len(q) == 0:                                 # 이렇게 돌면서 q에 담긴 놈들이 없으면 큰 무한루프 탈출
            break
    return new_graph                                    # 탐색된 그래프 리턴
    

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]     # 입력 그래프 생성


virus = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append((i,j))         # 바이러스 위치 파악 후 리스트에 저장
        elif graph[i][j] == 1:
            graph[i][j] = "-"           # 벽
            
time = int(1e9)                         # min값을 도출하기 위해 time의 초기값을 높은 값으로 설정

for v in list(itertools.combinations(virus,M)):     # 모든 경우의 수를 돌리면서 따져봐야하므로 조합 사용
    new_graph = bfs(v)                              # bfs 탐색
    max_time = find_max(new_graph)                  # bfs 탐색 후 나온 그래프를 체크 메소드 활용
    time = min(time, max_time)                      # 그래프 체크 메소드에서 나온 거리들을 비교하여 가장 작은 값을 도출

if time == int(1e9):                                # 바이러스가 다 안번진 경우를 뜻하므로
    print(-1)                                       # -1 을 출력
else:                                               # 바이러스가 다 돈 경우
    print(time - 1)                                     # time을 출력