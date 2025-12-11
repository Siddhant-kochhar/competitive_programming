'''
Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: We cannot type "world" because the 'd' key is broken.
Example 2:

Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.
'''

text ="leet code"
brokenLetters ="lt"


text_list = text.split()
print(text_list)

cnt = 0 
for i in text_list:
    if set(i) & set(brokenLetters):
            continue
        
    cnt += 1
print(cnt)