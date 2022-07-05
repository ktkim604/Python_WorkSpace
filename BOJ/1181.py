#단어 정렬
#다중 조건

n = int(input())
word_list = []
for i in range(n):
    word = input()
    word_list.append((len(word), word))

print("")
word_list = set(word_list)

a = sorted(word_list, key = lambda x : (x[0], x[1]))
for j in a:
    print(j[1])