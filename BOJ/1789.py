# 수들의 합
s = int(input())
sum = 0

for i in range(1, s+2):
    sum += i
    
    if sum == s:
        print(i)
        break
    
    elif sum > s:
        print(i-1)
        break