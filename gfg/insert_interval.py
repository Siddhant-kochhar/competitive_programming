intervals = [[1, 3], [4, 5], [6, 7], [8, 10]]
newInterval = [5, 6]

res = []
inserted = False

for i in intervals:
    if newInterval[1] < i[0]:
        res.append(newInterval)
        res += intervals[intervals.index(i):]
        inserted = True
        break
    elif newInterval[0] > i[1]:
        res.append(i)
    else:
        newInterval = (min(newInterval[0],i[0]),max(newInterval[1],i[1]))

# If newInterval was not inserted yet (comes after all intervals or was merged)
if not inserted:
    res.append(newInterval)

print(res)