sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

res = []

for i in sentences:
    res.append(len(i.split()))

print(max(res))