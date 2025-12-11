'''
2
5 5
2 2 1 3 2
2 3 3
2 3 4
1 5 5
1 4 9
2 4 3
10 5
1 1 1 1 1 1 1 1 1 1
3 8 13
2 5 10
3 8 10
1 10 2
1 9 100
'''

n = int(input())
for _ in range(n):
    m, q = map(int, input().split())
    x = list(map(int, input().split()))
    
    # Build prefix sum array
    prefix = [0] * (m + 1)
    for i in range(m):
        prefix[i + 1] = prefix[i] + x[i]
    
    total_sum = prefix[m]  # This is sum(x)
    
    for __ in range(q):
        l, r, v = map(int, input().split())
        # Calculate subarray sum using prefix sums in O(1)
        current_sum = prefix[r] - prefix[l - 1]
        new_addition = (r - l + 1) * v
        new_total_sum = total_sum - current_sum + new_addition
        
        if new_total_sum % 2 == 0:
            print("NO") 
        else:
            print("YES")



