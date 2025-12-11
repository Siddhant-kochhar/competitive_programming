'''
keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
'''

from collections import defaultdict


keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]

keyseen = defaultdict(list)
res = []


for i, j in zip(keyName, keyTime):
    sh, sm = map(int, j.split(":"))
    minutes = sh * 60 + sm
    keyseen[i].append(minutes)

for key,time in keyseen.items():
    time.sort()
    for z in range(len(time) - 2):
        if time[z+2] - time[z] <=60:
            res.append(key)

print(res)
