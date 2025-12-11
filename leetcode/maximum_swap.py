'''
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
'''

num = 98368
nums_list = list(str(num))
last = {int (d): i for i ,d enumerate(nums_list)}

for i, digit in enumerate(nums_list):
    for d in range(9,digit,-1):
        if last.get(d,-1) > i:
            num_list[i] , num_list[last[d]] = num_list[last[d]] , num_list[i]
            return int("".join(num_list))
return num

