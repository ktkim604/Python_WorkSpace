# 회의실 배정 (그리디, 다중조건)
n = int(input())

time_lsit = []
for _ in range(n):
    first, second = map(int, input().split())
    time_lsit.append([first, second])
    
time_lsit = sorted(time_lsit, key = lambda x : x[0])
time_lsit = sorted(time_lsit, key = lambda x : x[1])

last = 0
cnt = 0

for i,j in time_lsit:
    if i >= last:
        cnt += 1
        last = j
        
print(cnt)