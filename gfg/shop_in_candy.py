prices = [3, 2, 1, 4]
k = 2

prices_min = sorted(prices)
prices_max = sorted(prices, reverse=True)

price_min = 0 
price_max = 0

while prices_min:
    price_min += prices_min[0]
    prices_min.pop(0)
    print(price_min)
    if prices_min:  # Check if the list is not empty
        for i in range(min(k, len(prices_min))):  # Pop up to k elements or the remaining elements
            prices_min.pop(-1)

while prices_max:
    price_max += prices_max[0]
    prices_max.pop(0)
    if prices_max:  # Check if the list is not empty
        for i in range(min(k, len(prices_max))):  # Pop up to k elements or the remaining elements
            prices_max.pop(-1)

res = []
res.append(price_min)
res.append(price_max)
print(res)