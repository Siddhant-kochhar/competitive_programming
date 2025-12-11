'''
An array 𝑏1,𝑏2,…,𝑏𝑛
 of positive integers is good if all the sums of two adjacent elements are equal to the same value. More formally, the array is good if there exists a 𝑘
 such that 𝑏1+𝑏2=𝑏2+𝑏3=…=𝑏𝑛−1+𝑏𝑛=𝑘
.

Doremy has an array 𝑎
 of length 𝑛
. Now Doremy can permute its elements (change their order) however she wants. Determine if she can make the array good.
'''

from collections import Counter

def helper(nums):
    count = Counter(nums)
    if len(count) > 2:
        return "No"
    elif len(count) == 1:
        return "Yes"
    else:
        vals = list(count.values())
        if abs(vals[0] - vals[1]) <= 1:
            return "Yes"
        else:
            return "No"

t = int(input())  # number of test cases
for _ in range(t):
    n = int(input())  # length of array
    nums = list(map(int, input().split()))
    print(helper(nums))
