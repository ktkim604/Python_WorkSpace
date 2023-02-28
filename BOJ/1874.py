# 스택 수열
n = int(input())
ans = []
stack = []
cnt = 1
flag = 0

for i in range(n):
    num = int(input())
    
    for j in range(cnt, num+1):
        stack.append(j)
        ans.append('+')
        cnt += 1
        if cnt >= num:
            continue
        
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
        
    else:
        print('NO')
        flag = 1
        break
        
if flag == 0:
   for i in ans:
       print(i)
        