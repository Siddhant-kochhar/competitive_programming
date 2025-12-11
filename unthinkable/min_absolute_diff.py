arr = [40,11,26,27,-20]
res = []

def min_absolute_diff(arr, res):
    arr.sort()
    min_diff = min(arr[i + 1] - arr[i] for i in range(0, len(arr) - 1))
    for i in range(0, len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        if diff == min_diff:
            res.append([arr[i], arr[i + 1]])
        else:
            continue
    return res

print(min_absolute_diff(arr, res))