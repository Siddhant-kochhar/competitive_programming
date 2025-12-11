'''
Input: n = 9
Output: 2
Explanation: Many paths are possible from 1 to 9. Shortest one possible is, 1 -> 3 -> 9, of length 2.
Input: n = 4
Output: 2
Explanation: Possible paths from 1 to 4 are, 1 -> 2 -> 3 -> 4 and 1 -> 3 -> 4. Second path of length 2 is the shortest.
'''

n = 15
res = []
i = 1 

while i <= n:
    res.append(i)
    print(res)
    if i * 3 <= n:
        i *= 3
    else:
        i += 1

print(len(res) - 1) 
