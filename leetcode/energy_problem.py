energy = [-2,-3,-1]
k = 2
l = 0
n = len(energy)

dp = energy.copy()

for i in range(len(energy)-1,-1,-1):
    if i + n < k:
        dp[i] = dp[i+k]

print(max(dp))