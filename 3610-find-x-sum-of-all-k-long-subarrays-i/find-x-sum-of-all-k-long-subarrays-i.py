class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        left = 0 
        window = nums[left:k]
        count = Counter(window)
        max_heap = [(-freq,-num) for num,freq in count.items()]
        heapq.heapify(max_heap)
        result = []
        result.append(sum([-num * -freq for freq, num in heapq.nsmallest(x, max_heap)]))
        for r in range(k,len(nums)):
            left_num = nums[left]
            count[left_num] -= 1
            if count[left_num] == 0:
                del count[left_num]
            right_num = nums[r]
            count[right_num] += 1
            max_heap = [(-freq,-num) for num,freq in count.items()]
            heapq.heapify(max_heap)
            result.append(sum([-num * -freq for freq, num in heapq.nsmallest(x, max_heap)]))
            left += 1
        return result