# 문자열

a, b = map(str, input().split())
# count = 0

# if len(a) == len(b):
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             count += 1
#     print(count)
      
# elif a in b:
#     print(0)
answer = 1000
for i in range((len(b)-len(a))+1):
    temp = b[i:i+len(a)]
    cnt = 0
    for x, y in zip(a, temp):
        if x != y:
            cnt += 1
    if cnt < answer:
        answer = cnt
        
print(answer)