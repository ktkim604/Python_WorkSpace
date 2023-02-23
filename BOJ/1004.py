# 어린 왕자
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cnt = 0
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    for i in range(N):
        cx, cy, r = map(int, input().split())

        d1 = (cx-x1)**2 + (cy-y1)**2
        d2 = (cx-x2)**2 + (cy-y2)**2
        pow_r = r**2
        
        if d1 >= pow_r and d2 >= pow_r:
            pass
        elif d1 >= pow_r:
            cnt += 1
        elif d2 >= pow_r:
            cnt += 1
        
    print(cnt)