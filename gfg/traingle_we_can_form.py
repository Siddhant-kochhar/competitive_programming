def countTriangles(arr):
    arr.sort()
    n = len(arr)
    count = 0

    for k in range(n-1, 1, -1):   # fix largest side
        i, j = 0, k-1
        while i < j:
            if arr[i] + arr[j] > arr[k]:
                count += (j - i)   # all between i..j-1 are valid
                j -= 1
            else:
                i += 1
    return count


# Example
arr = [4, 6, 3, 7]
print(countTriangles(arr))  # Output: 3


'''
[3,4,6,7]
k in range(3, 1, -1)
i = 0
j = 2
0 < 2 :
arr[0] + arr[2] > arr[3]  (4 + 6 > 7)  : true