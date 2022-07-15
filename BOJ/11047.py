# 동전 O

n1, n2 = map(int, input().split())
m_list = []

for i in range(n1):
    m = int(input())
    if m <= n2:
        m_list.append(m)
        
m_list = sorted(m_list, reverse=True)
sum = 0

for j in m_list:
    a = n2 // j
    b = n2 % j
    n2 = b
    sum += a
    
print(sum)