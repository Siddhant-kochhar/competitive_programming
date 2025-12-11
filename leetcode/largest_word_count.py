'''
Input: messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], senders = ["Alice","userTwo","userThree","Alice"]
Output: "Alice"
Explanation: Alice sends a total of 2 + 3 = 5 words.
userTwo sends a total of 2 words.
userThree sends a total of 3 words.
Since Alice has the largest word count, we return "Alice".
'''

from collections import defaultdict 

messages = ["How is leetcode for everyone","Leetcode is useful for practice"]
senders =["Bob","Charlie"]


merged = defaultdict(list)

for i,j in zip(messages,senders):
    merged[j].append(len(i.split()))

for key,value in merged.items():
    merged[key] = sum(value)

merged = dict(sorted(merged.items(), key=lambda x: x[1], reverse=True))

max_count = max(merged.values())
candidates = [name for name, count in merged.items() if count == max_count]
print(max(candidates))
