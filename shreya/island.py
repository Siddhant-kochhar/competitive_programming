import sys

def max_value(N, K, V):
    if N < K:
        return 0
    
    if N == 1:
        return V[0][0] if K == 1 else 0
    
    max_result = 0
    
    # Try each possible type for the first island
    for first_type in range(K):
        # Use memoization for the remaining islands
        memo = {}
        
        def solve(island, last_type, used_mask):
            if island == N:
                # Check if all types are used
                return 0 if used_mask == (1 << K) - 1 else float('-inf')
            
            if (island, last_type, used_mask) in memo:
                return memo[(island, last_type, used_mask)]
            
            best = float('-inf')
            
            for curr_type in range(K):
                # Cannot use same type as previous island
                if curr_type == last_type:
                    continue
                
                # If this is the last island, cannot use same type as first island
                if island == N - 1 and curr_type == first_type:
                    continue
                
                new_mask = used_mask | (1 << curr_type)
                value = V[island][curr_type] + solve(island + 1, curr_type, new_mask)
                best = max(best, value)
            
            memo[(island, last_type, used_mask)] = best
            return best
        
        # Start from island 1 (second island) since we fixed the first island
        first_mask = 1 << first_type
        result = V[0][first_type] + solve(1, first_type, first_mask)
        
        if result > max_result:
            max_result = result
    
    return max_result if max_result > 0 else 0

def main():
    N = int(sys.stdin.readline().strip())
    K = int(sys.stdin.readline().strip())
    
    V = []
    for i in range(N):
        V.append(list(map(int, sys.stdin.readline().strip().split())))
    
    result = max_value(N, K, V)
    print(result)

if __name__ == "__main__":
    main()