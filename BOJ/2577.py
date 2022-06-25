A = int(input())
B = int(input())
C = int(input())

N = A*B*C
result = list(str(N))
for i in range(10):
    print(result.count(str(i)))

