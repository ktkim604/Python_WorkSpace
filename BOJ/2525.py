A, B = map(int, input().split())
C = int(input())

N = A*60 + B + C
A = N//60
B = N%60
if (A >= 24):
    A = A-24
print(A, B)