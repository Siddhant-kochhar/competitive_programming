def max_points_game(points):
    n = len(points)
    if n == 0:
        return 0
    if n == 1:
        return points[0]
    
    max_total = 0
    
    # Try starting from each level
    for start in range(n):
        # For subarray starting from 'start', find max sum of non-adjacent elements
        if start == n - 1:
            # Only one element left
            total = points[start]
        else:
            # Dynamic programming for non-adjacent sum starting from 'start'
            sub_points = points[start:]
            sub_n = len(sub_points)
            
            if sub_n == 1:
                total = sub_points[0]
            else:
                # dp[i] represents max sum we can get from sub_points[i:]
                dp = [0] * sub_n
                dp[sub_n - 1] = sub_points[sub_n - 1]  # Last element
                dp[sub_n - 2] = max(sub_points[sub_n - 2], sub_points[sub_n - 1])  # Second last
                
                # Fill dp array backwards
                for i in range(sub_n - 3, -1, -1):
                    dp[i] = max(dp[i + 1], sub_points[i] + dp[i + 2])
                
                total = dp[0]
        
        max_total = max(max_total, total)
    
    return max_total

# Read input
n = int(input())
points = list(map(int, input().split()))

# Solve and print result
result = max_points_game(points)
print(result)