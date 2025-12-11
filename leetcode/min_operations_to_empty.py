from collections import Counter

nums = [2,3,3,2,2,4,2,3,4]

nums_dict = Counter(nums)
print(nums_dict)


res = 0 
cnt = 0 
for i in nums_dict.items():
    if i %3 == 0 and i !=0:
        cnt += 1 
        i //=3 
    elif i % 2 ==0 and i != 0:
        cnt += 1 
        i //= 2 
    else:
        print(-1)
        break
res += cnt
print(res)