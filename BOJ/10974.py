# 모든 순열
from itertools import permutations

n = int(input())
num_list = [i for i in range(1, n+1)]

permu = list(permutations(num_list))

for per in permu:
    for N in per:
        if N == per[-1]:
            print(N)
        else:
            print(N, end=' ')