# 최소 힙 
import sys
import heapq
input = sys.stdin.readline

heap = []

for i in range(int(input())):
    n = int(input())

    if n == 0:
        if len(heap):  # 힙이 비어있을때 heappop 메소드 호출하면 오류발생 함.
            print(heapq.heappop(heap)) 
        else:
            print(0)
            
    else:
        heapq.heappush(heap, n)
        
