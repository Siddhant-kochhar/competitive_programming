arr = [3, 1, 2, 4]
n = len(arr)
nsl = [-1] * n
nsr = [n] * n

stack = []

# NSL
for i in range(n):
    while stack and arr[stack[-1]] >= arr[i]:
        stack.pop()
    if stack:
        nsl[i] = stack[-1]
    stack.append(i)

# Clear stack for NSR
stack = []

# NSR
for i in range(n - 1, -1, -1):
    while stack and arr[stack[-1]] > arr[i]:
        stack.pop()
    if stack:
        nsr[i] = stack[-1]
    stack.append(i)

print("NSL:", nsl)  # Expected: [-1, -1, 1, 2]
print("NSR:", nsr)  # Expected: [1, 4, 4, 4]

# Contribution calculation
res = 0
for idx in range(n):
    left_count = idx - nsl[idx]
    right_count = nsr[idx] - idx
    res += arr[idx] * left_count * right_count

print("Sum of subarray minimums:", res)  # Expected: 17
