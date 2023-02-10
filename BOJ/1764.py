# 듣보잡
N, M = map(int, input().split())

listen = [input() for _ in range(N)]
see = [input() for _ in range(M)]

listen2 = set(listen)
see2 = set(see)

ans = sorted(list(listen2 & see2))

print(len(ans), *ans, sep='\n')