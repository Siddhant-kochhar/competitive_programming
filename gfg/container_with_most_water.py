arr = [3, 1, 2, 4, 5]

left = 0    
right = len(arr) - 1
max_area = float('-inf')

while left < right:
    area = min(arr[left], arr[right]) * (right - left)
    max_area = max(max_area, area)
    if arr[left] < arr[right]:
        left += 1
    else:
        right -= 1

print(max_area)