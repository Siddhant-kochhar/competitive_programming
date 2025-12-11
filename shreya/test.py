text = "hello world"
brokenLetters = "ad"

new_t = text.split()
# print(new_t)
li = list(brokenLetters)
# print(li)
cnt = 0
for i in range(len(new_t)):
    correct_word = True #assume the word is correct
    for j in range(len(li)):
        if li[j] in new_t[i]:
            correct_word = False #if j in i then it is a broken letter
            break
    if correct_word: 
        cnt += 1
print(cnt)