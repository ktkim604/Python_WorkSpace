# 요세푸스 문제
from collections import deque

N, K = map(int, input().split())
q = [i for i in range(1, N+1)]

for i in range(N):
    
    dq = deque(q)
    dq.rotate(K+2)
    q = list(dq)
    

    print(q)
