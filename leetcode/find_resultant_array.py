from collections import Counter as counter

words = ["a","b","c","d","e"]
res = [words[0]]

for i in range(1,len(words)):
    if sorted(counter(words[i])) != sorted(counter(words[i-1])):
        res.append(words[i])

print(res)