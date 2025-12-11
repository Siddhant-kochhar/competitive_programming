'''
Input: s1 = "AXY", s2 = "YADXCP"
Output: false
Explanation: s1 is not a subsequence of s2 as 'Y' appears before 'A'.
Input: s1 = "gksrek", s2 = "geeksforgeeks"
Output: true
Explanation: If we combine the bold character of "geeksforgeeks", it equals to s1. So s1 is a subsequence of s2. 
'''

s1 = "ABC"
s2 = "AFBHC"

s1_left = 0
s2_left = 0

while s1_left < len(s1) and s2_left < len(s2):
    if s1[s1_left] == s2[s2_left]:
        s1_left += 1
    s2_left += 1

if s1_left == len(s1):
    print("true")
else:
    print("false")
