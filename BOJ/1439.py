# 뒤집기

s = list(input())
count = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count += 1
      
change_min_cnt = (count+1)//2  

print(change_min_cnt) 