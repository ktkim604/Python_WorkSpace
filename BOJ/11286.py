# 절댓값 힙
import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    
    if x == 0:
        if len(heap):
            print(heapq.heappop(heap)[1])  
        else:
            print(0)    
    else:
        heapq.heappush(heap, (abs(x), x))             # 힙을 튜플로 구성
        