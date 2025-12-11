def longestPathInGrid(N, M, grid):
    dp = [[-1] * M for _ in range(N)]
    dp[N-1][M-1] = 1
    
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if i == N-1 and j == M-1:
                continue
            candidates = []
            # Check right neighbor
            if j + 1 < M and grid[i][j] < grid[i][j+1] and dp[i][j+1] != -1:
                candidates.append(1 + dp[i][j+1])
            # Check down neighbor
            if i + 1 < N and grid[i][j] < grid[i+1][j] and dp[i+1][j] != -1:
                candidates.append(1 + dp[i+1][j])
            if candidates:
                dp[i][j] = max(candidates)
            else:
                dp[i][j] = -1
                
    return dp[0][0] if dp[0][0] != -1 else -1










SELECT 
    c.customer_name,
    o.order_id,
    o.order_date,
    COUNT(DISTINCT oi.product_id) AS product_count,
    o.total_amount AS order_total
FROM 
    orders o
JOIN 
    customers c ON o.customer_id = c.customer_id
LEFT JOIN 
    order_items oi ON o.order_id = oi.order_id
GROUP BY 
    c.customer_name, o.order_id, o.order_date, o.total_amount
ORDER BY 
    o.order_date DESC, c.customer_name ASC;