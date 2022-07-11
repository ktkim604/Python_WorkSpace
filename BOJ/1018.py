#체스판 다시 칠하기
n1, n2 = map(int, input().split())
orginal = []
count = []

for i in range(n1):
    orginal.append(input())

for j in range(n1-7):
    for k in range(n2-7):
        index_W = 0
        index_B = 0
        for l in range(j, j+8):
            for m in range(k, k+8):
                if (l + m) % 2 == 0:
                    if orginal[l][m] != 'W':
                        index_W += 1
                    if orginal[l][m] != 'B':
                        index_B += 1
                else:
                    if orginal[l][m] != 'B':
                        index_W += 1
                    if orginal[l][m] != 'W':
                        index_B += 1
        count.append(min(index_W,index_B))
        
print(min(count))            
                
            
        