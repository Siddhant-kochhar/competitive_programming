m = 3
k = 2
arr = [3, 4, 2, 7, 13, 8, 5]

n = len(arr)
if n < m * k:
    print(-1)
    exit()

start_day = 1 
end_day = max(arr)  
ans = end_day

def canMakeBouquets(day, m, k, arr):
    bouquet = 0 
    consecutive = 0 
    for i in range(len(arr)):
        if arr[i] <= day:
            consecutive += 1
            if consecutive == k:
                bouquet += 1
                consecutive = 0
        else:
            consecutive = 0
    return bouquet >= m

while start_day <= end_day:
    mid = (start_day + end_day) // 2
    if canMakeBouquets(mid, m, k, arr):
        ans = mid
        end_day = mid - 1
    else:
        start_day = mid + 1

print(ans)