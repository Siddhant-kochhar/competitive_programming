class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        pse = [-1] * n
        nse = [n] * n 
        MOD = 10**9 + 7

        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)

        stack = []

        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]] > arr[i] :
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)

        ans = 0 
        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i
            ans = (ans + arr[i] * left * right) % MOD

        return (ans)
