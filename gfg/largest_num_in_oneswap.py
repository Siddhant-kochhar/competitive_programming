'''
Input: s = "768"
Output: "867"
Explanation: Swapping the 1st and 3rd characters(7 and 8 respectively), gives the lexicographically largest string.
Input: s = "333"
Output: "333"
Explanation: Performing any swaps gives the same result i.e "333".
'''

s = "867"
s_list = list(s)
print(s_list)
n = len(s_list)

max_seen = [0]*n
max_seen[n-1] = n-1  


for i in range(n-2, -1, -1):
    if s_list[i] < s_list[max_seen[i+1]]:
        max_seen[i] = max_seen[i+1]   
    else:
        max_seen[i] = i
print(max_seen)   

for i in range(n):
    if s_list[i] < s_list[max_seen[i]]:
        s_list[i], s_list[max_seen[i]] = s_list[max_seen[i]], s_list[i]
        break
print("".join(s_list))


