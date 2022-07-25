n = int(input())

number = []
for i in range(n):
    a, b = map(int, input().split())
    number.append((a,b))
    
number.sort(key = lambda x : (x[0], x[1]))

for j in number:
    print(j[0], j[1])    
