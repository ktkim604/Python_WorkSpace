n, k = map(int, input().split())

result = 0

while bin(n).count('1') > k:
    p = 2 ** (bin(n))[::-1].index('1')
    result += p
    n += p
    
print(result)

