from collections import Counter

nums = [1,3,4,1,2,3,1]
nums_dict = Counter(nums)
two_d = []


while len(nums_dict) > 0:
    res = []
    keys_to_process = list(nums_dict.keys())
    for key in keys_to_process:
        
        res.append(key)
        nums_dict[key] -= 1

        if nums_dict[key] == 0:
            del[nums_dict[key]]
    two_d.append(res)

print(two_d)

     
