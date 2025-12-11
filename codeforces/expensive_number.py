x = list("666")

left = 0 
right = len(x) - 1

count = 0
while left <= right:
    if left < len(x):
        x.pop(left)
        count += 1
    if right < len(x) and left <= right:
        x.pop(right - 1)
        count += 1
        right -= 2
    else:
        right -= 1

print(count)
