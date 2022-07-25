n = int(input())

info = []
for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    info.append((age, name))
    
info.sort(key = lambda x : x[0])

for j in info:
    print(j[0], j[1])

