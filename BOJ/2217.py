n = int(input())

rope = []
result = []

for i in range(n):
    m = int(input())
    rope.append(m)
    
rope = sorted(rope, reverse=True)

for j in range(n):
    result.append(rope[j] * (j+1))
    
print(max(result))