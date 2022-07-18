# 회의실 배정 (그리디, 다중조건)
n = int(input())

time_list = []
for _ in range(n):
    first, second = map(int, input().split())
    time_lsit.append([first, second])
    
time_list = sorted(time_list, key = lambda x : x[0])
time_list = sorted(time_list, key = lambda x : x[1])

last = 0
cnt = 0

for i,j in time_list:
    if i >= last:
        cnt += 1
        last = j
        
print(cnt)