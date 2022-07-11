#체스판 다시 칠하기
n1, n2 = map(int, input().split())
for i in range(n1):
    for j in range(n2):
        print('*', end ='')
        if j == n2-1:
            print()
       