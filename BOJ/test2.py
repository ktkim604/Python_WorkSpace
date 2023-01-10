import sys
input = sys.stdin.readline

N = int(input())
L = [0] + list(map(int, input().split()))
P = [0] + list(map(int, input().split()))
dp = [0 for _ in range(101) for _ in range(N+1)]

print(dp)

# for i in range(1, N+1):
    