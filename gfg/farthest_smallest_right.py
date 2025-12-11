'''
Input: arr[] = [2, 5, 1, 3, 2]
Output: [2, 4, -1, 4, -1]
Explanation: arr[0] = 2: Farthest smaller element to the right is arr[2] = 1.
arr[1] = 5: Farthest smaller element to the right is arr[4] = 2.
arr[2] = 1: No smaller element to the right → -1.
arr[3] = 3: Farthest smaller element to the right is arr[4] = 2.
arr[4] = 2: No elements to the right → -1.
'''

x = [2, 5, 1, 3, 2]
res = [-1] * len(x)

i = 0 
while i < len(x):
   
    for j in range(len(x)-1, i, -1):
        if x[j] < x[i]:
            res[i] = j 
            break   
    i += 1

print(res)



res = [-1] * n
stack = []

# Process from right to left
for i in range(n-1, -1, -1):
    # Pop elements from stack that are not smaller than current element
    # We want to maintain a stack with decreasing values
    while stack and x[stack[-1]] >= x[i]:
        stack.pop()
    
    # If stack is not empty, the top element is the farthest smaller to the right
    if stack:
        res[i] = stack[-1]
    else:
        res[i] = -1
    
    # Push current index to stack
    stack.append(i)

print(res)