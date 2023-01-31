# 연구소
import sys
from collections import deque
import copy

def wall(wall_cnt):
    if wall_cnt == 3:                       # 벽 3개를 다 세웠을 때         
        bfs()
        return
    
    for i in range(n):                      # 안전영역에 벽을 3개 세워보는 모든 경우
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(wall_cnt+1)            # 그냥 조합으로 풀자 재귀로 까불지마고
                # 재귀가 끝나면 최대로 3개의 벽을 세울수 있어서 다른곳도 세워보기 위해서 벽을 허문다.
                graph[i][j] = 0

def bfs():                                  # 바이러스 퍼지게 하는 메소드
    global answer                           # 전역변수 answer 지역변수에서 사용해야하므로 글로벌로 변수 선언
    copy_graph = copy.deepcopy(graph)       # 해당 bfs를 돌때마다 해당 graph 원본 유지
    
    q = deque()
    for i in range(n):
        for j in range(m):  
            if copy_graph[i][j] == 2:       # 해당 좌표에 바이러스가 있을때 어팬드
                q.append((i,j))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and copy_graph[nx][ny] == 0:
                copy_graph[nx][ny] = 2
                q.append((nx,ny))
    
    safe_cnt = 0                            # 안전영역 갯수를 구하기 위한 변수 설정
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 0:       # 안전영역인 0의 갯수를 다 더해줌
                safe_cnt += 1
    answer = max(answer, safe_cnt)          # 벽을 3개 세운 모든 경우중에서 안전영역의 크기가 가장 큰 놈을 도출
                
                
n, m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer = 0
wall(0)
print(answer)




