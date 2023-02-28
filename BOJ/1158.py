# 요세푸스 문제
N, K = map(int, input().split())

q = [i for i in range(1, N+1)]
dq = []
key = 0

while q:
    key = (key + (K-1)) % len(q)
    temp = q.pop(key)
    dq.append(str(temp))
    
print('<%s>' %(', '.join(dq)))