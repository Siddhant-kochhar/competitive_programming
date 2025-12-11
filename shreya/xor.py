import sys

def get_ans(N, A, Len):
    MOD = 10**9 + 7
    
    # Find all valid ranges with XOR = 0
    valid_ranges = []
    
    # Efficient XOR range finding
    for i in range(N):
        xor_val = 0
        for j in range(i, N):
            xor_val ^= A[j]
            if xor_val == 0:
                length = j - i + 1
                if length <= Len[j]:
                    valid_ranges.append((i, j))
    
    # Sort ranges by ending position for interval scheduling
    valid_ranges.sort(key=lambda x: x[1])
    
    # Dynamic programming for weighted interval scheduling
    # dp[i] = maximum sum we can make zero considering ranges 0 to i
    n = len(valid_ranges)
    
    if n == 0:
        return sum(A) % MOD
    
    # For each range, calculate the sum it covers
    range_sums = []
    for start, end in valid_ranges:
        range_sum = sum(A[start:end+1])
        range_sums.append(range_sum)
    
    # Find the latest non-overlapping range for each range
    compatible = [-1] * n
    for i in range(n):
        for j in range(i-1, -1, -1):
            if valid_ranges[j][1] < valid_ranges[i][0]:
                compatible[i] = j
                break
    
    # DP to find maximum sum we can zero out
    dp = [0] * n
    dp[0] = range_sums[0]
    
    for i in range(1, n):
        # Option 1: Don't take current range
        dp[i] = dp[i-1]
        
        # Option 2: Take current range
        current_sum = range_sums[i]
        if compatible[i] != -1:
            current_sum += dp[compatible[i]]
        
        dp[i] = max(dp[i], current_sum)
    
    # The answer is total sum minus maximum sum we can zero out
    total_sum = sum(A)
    max_zero_sum = dp[n-1] if n > 0 else 0
    
    return (total_sum - max_zero_sum) % MOD

def main():
    N = int(sys.stdin.readline().strip())
    A = []
    for _ in range(N):
        A.append(int(sys.stdin.readline().strip()))
    
    Len = []
    for _ in range(N):
        Len.append(int(sys.stdin.readline().strip()))
    
    result = get_ans(N, A, Len)
    print(result)

if __name__ == "__main__":
    main()=