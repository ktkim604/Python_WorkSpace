# 최대 힙 -> 부호를 변경하는 방식을 사용하여 최대 힙 구함
import sys
import heapq
input = sys.stdin.readline

max_heap = []

for i in range(int(input())):
    n = int(input())
    
    if n == 0:
        if len(max_heap):
            print(-heapq.heappop(max_heap))
        else:
            print(0)
            
    else:
        heapq.heappush(max_heap, -n)