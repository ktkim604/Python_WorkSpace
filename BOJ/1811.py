n1, n2, n3 = map(int, input().split())

a_list = []
for i in range(n1):
    a = list(map(int, input().split()))
    a_list.append(a)
    print(a_list, i)