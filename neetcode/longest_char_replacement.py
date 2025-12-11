'''
Input: s = "XYYX", k = 2
Output: 4
'''
from collections import defaultdict

s = "XYYX"
k = 2

def char_replacement(s,k):
    left = 0 
    freq = defaultdict(int)
    length = float('-inf')

    for right in range(len(s)):
        freq[s[right]] += 1
        if (right-left+1) - max(freq.values()) > k:
            freq[s[left]] -= 1
            left += 1
    length = max(length, right - left + 1)
    return length
print(char_replacement(s, k))