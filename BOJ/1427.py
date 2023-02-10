# 소트인사이드

temp = list(map(int, input().strip()))

temp.sort(reverse=True)

for i in temp:
    print(i, end='')