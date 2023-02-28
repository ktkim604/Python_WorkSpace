# 뒤집기
# 그리디 문제 -> 문제해서 제시하는 입력들을 하나씩 나열해보며 규칙성을 파악하자

s = list(input())
count = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count += 1
      
change_min_cnt = (count+1)//2  

print(change_min_cnt) 