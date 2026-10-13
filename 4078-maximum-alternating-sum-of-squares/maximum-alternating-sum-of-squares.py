class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums_pos = [abs(i) for i in nums ]
        nums_pos.sort()
        print(nums_pos)
        left = 0 
        right = len(nums_pos) - 1

        ans = 0 
        flag = True
        while left <= right:
            if flag:
                if nums_pos[right] > nums_pos[left]:
                    ans += nums_pos[right] **2
                    right -= 1
                else:
                    ans += nums_pos[left] **2
                    left += 1
            else:
                if nums_pos[right] > nums_pos[left]:
                    ans -= nums_pos[left] **2
                    left += 1
                else:
                    ans -= nums_pos[right] **2
                    right -= 1 
            flag = not flag
            

        return (ans)