def is_prime(n):
    if n<= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_mega_prime(left,right,res):
    for n in range(left, right + 1):
        if not is_prime(n):
            continue
        temp = n
        is_mega = True
        while temp > 0:
            digit = temp % 10
            if not is_prime(digit):
                is_mega = False
                break
            temp //= 10
        if is_mega:
            res.append(n)
    return res

result = is_mega_prime(10, 30, [])
print(result)