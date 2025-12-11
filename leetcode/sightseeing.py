values = [1, 2]
left = 0 
right = len(values) - 1

max_seen = float("-inf")

while left < right:
    max_seen = max(values[left] + values[right] + left - right, max_seen)
    
    if values[left] > values[right]:
        right -= 1
    elif values[left] < values[right]:
        left += 1
    else:  # values[left] == values[right]
        if left + 1 > right - 1:
            left += 1
        else:
            right -= 1

print(max_seen)
