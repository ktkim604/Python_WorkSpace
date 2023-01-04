n = list(input())
n.sort(reverse=True)
list_n = list(map(int, n))

if list_n[-1] != 0 or sum(list_n)%3 != 0:
    print(-1)

else:
    print(''.join(map(str, list_n)))