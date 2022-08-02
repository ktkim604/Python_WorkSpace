import sys
n1, n2 = map(int, sys.stdin.readline().split())

prime_num = []

for i in range(n1, n2+1):
    list = []
    for j in range(1, int(i**0.5)+1):
        if i % j == 0:
            list.append(j)
    if len(list) == 2:
        prime_num.append(i)
        
print(prime_num)

# import sys
# n1, n2 = map(int, sys.stdin.readline().split())

# for i in range(n1, n2+1):
#     if i == 1:
#         continue
#     for j in range(2, int(i**0.5)+1):
#         if i % j == 0:
#             break
#     else:
#         print(i)
        
            
