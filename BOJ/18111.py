# 마인크래프트
import sys

n, m, b = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
answer = 100000000000


for target in range(257):
    max, min = 0, 0
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= target:
                max += graph[i][j] - target
                
            else:
                min += target - graph[i][j]
    print(max, min)
    if max + b >= min:
        if min + (max * 2) <= answer:
            answer = min + (max * 2)
            floor = target
            
print(answer, floor)