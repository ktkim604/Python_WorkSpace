#ATM

n = int(input())
m = list(map(int, input().split()))

m = sorted(m)
num = 0

for i in range(n):
    num += sum(m[0:i+1])
    
print(num)
    
# for i in range(n):
#     for j in range(i + 1):
#         num += m[j]
    
# print(num)


