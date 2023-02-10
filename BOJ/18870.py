# 좌표 압축

N = int(input())

temp = list(map(int, input().split()))

ans = sorted(set(temp))

dict = {}
for i in range(len(ans)):
    dict[ans[i]] = i
    
print(dict)
for i in temp:
    print(dict[i], end=' ')