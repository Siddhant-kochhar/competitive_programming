'''
Let's call a positive integer extremely round if it has only one non-zero digit. For example, 5000
, 4
, 1
, 10
, 200
 are extremely round integers; 42
, 13
, 666
, 77
, 101
 are not.

You are given an integer 𝑛
. You have to calculate the number of extremely round integers 𝑥
 such that 1≤𝑥≤𝑛
.
'''

def check(x):
    count_of_digits = 0
    count_of_zeros = 0 
    while x:
        if x%10 == 0 :
            count_of_zeros += 1 
        count_of_digits += 1 
        x //=10
    return count_of_zeros == count_of_digits-1

round_numbers = []
for i in range(1, 10**6):
    if check(i):
        round_numbers.append(i)

t = int(input())
for _ in range(t):
    n = int(input())
    answer = 0 
    for num in round_numbers:
        if num <= n:
            answer += 1
        else:
            break
    print(answer)