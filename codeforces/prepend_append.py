t = int(input())

for _ in range(t):
    final_lenght = int(input())
    num_str = (input())
    left = 0 
    right = len(num_str)-1

    while left < right:
        if (num_str[left] == "1" and num_str[right] == "0") or (num_str[left] == "0" and num_str[right] == "1"):
            left += 1
            right -= 1
        else:
            break

    print(right-left+1)