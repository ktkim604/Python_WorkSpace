# 숫자 정사각형
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(N)]

temp = []
if N <= M:
    for i in range(N):
        for j in range(N-i):
            for k in range(M-i):
                if graph[j][k] == graph[j][k+i] == graph[j+i][k] == graph[j+i][k+i]:
                    size = (i+1) * (i+1)
                    temp.append(size)

    print(max(temp))
    
else:
    for i in range(M):
        for j in range(N-i):
            for k in range(M-i):
                if graph[j][k] == graph[j][k+i] == graph[j+i][k] == graph[j+i][k+i]:
                    size = (i+1) * (i+1)
                    temp.append(size)
                    
    print(max(temp))