num = []

for i in range(10):
    a = int(input())
    b = a % 42
    num.append(b)

s = set(num) #자료형에서 중복을 제거
print(len(s))

