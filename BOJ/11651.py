n = int(input())

number = []

for i in range(n):
    x, y = map(int, input().split())
    number.append((x, y))
    
number.sort(key = lambda x : (x[1], x[0]))

for j in number:
    print(j[0], j[1])