# 단어나누기 (브루트 포스)

word = list(input())
division_word = []
join_word = []

for i in range(1, len(word)-1) :
    for j in range(i+1, len(word)):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        division_word.append(a+b+c)

for k in division_word:
    join_word.append(''.join(k))
    
print(sorted(join_word)[0])
