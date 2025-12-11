import math

def min_robbing(n, h, houses):
    def can_rob_all(k):
        """Check if Charlie can rob all houses with speed k houses/hour in h hours"""
        total_hours_needed = 0
        for house_count in houses:
            # Time needed for this street = ceil(house_count / k)
            hours_for_street = math.ceil(house_count / k)
            total_hours_needed += hours_for_street
        return total_hours_needed <= h
    
    # Binary search for minimum k
    left = 1
    right = max(houses)  # Maximum houses in any street
    
    while left < right:
        mid = (left + right) // 2
        if can_rob_all(mid):
            right = mid  # mid works, try smaller values
        else:
            left = mid + 1  # mid doesn't work, need larger values
    
    return left

# Read input
n, h = map(int, input().split())
houses = list(map(int, input().split()))

# Calculate and print result
result = min_robbing(n, h, houses)
print(result)