n = int(input())

def is_even(n):
    if n > 2:
        if n%2 ==0:
            return "Yes"
        else:
            return "No"
    return "No"

print(is_even(n))