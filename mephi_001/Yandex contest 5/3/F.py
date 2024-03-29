dict_words = set(input().split())
words = input().split()
result = []
for word in words:
    tag = 1
    for i in range(len(word)):
        if word[0:i] in dict_words:
            result.append(word[0:i])
            tag = 0
            break
    if tag:
        result.append(word)
print(*result)
