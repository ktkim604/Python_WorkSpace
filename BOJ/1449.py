# 수리공 항승

N, L = map(int, input().split())
water = list(map(int, input().split()))
water.sort()

cnt = 1
start = water[0]

for location in water:
    if location in range(start, start + L):
        continue
    
    else:
        start = location
        cnt += 1
        
print(cnt)
    