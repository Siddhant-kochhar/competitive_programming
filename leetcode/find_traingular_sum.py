nums = [2,6,6,5,5,3,3,8,6,4,3,3,5,1,0,1,3,6,9]

temp = []

if len(nums) > 1:
    while len(nums) > 1:
        for i in range(len(nums)- 1):
            x = (nums[i]+nums[i+1])
            print(x)
            if x > 10:
                temp.append(int(str(x)[-1]))
            else:
                temp.append(x)
        nums.clear()
        nums = temp.copy()
        print(temp)
        print(nums)
        temp.clear()
    if nums[0] > 10:
        print(int(str(x)[0]))
    else:
        print(nums[0])
else:
    print(nums[0])