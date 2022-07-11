t = int(input())
list = []

for i in range(t):
    n1, n2 = map(int, input().split())
    list.append((n1, n2))
    
for j in list:
    rank = 1
    for k in list:
        if j[0] < k[0] and j[1] <k[1]:
            rank += 1
    print(rank, end = " ")