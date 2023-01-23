# 스택 수열
n = int(input())
ans = []
stack = []
cnt = 1
flag = 0

for i in range(n):
    num = int(input())
    
    while cnt <= num:
        stack.append(cnt)
        ans.append('+')
        cnt += 1
        
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
        
    else:
        print('NO')
        flag = 1
        
if flag == 0:
   for i in ans:
       print(i)
        