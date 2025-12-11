import itertools

n = 3
result = [''.join(map(str, combo)) for combo in itertools.product([0, 1], repeat=n)]
print(result)  # Output: ['000', '001', '010', '011', '100', '101', '110', '111']