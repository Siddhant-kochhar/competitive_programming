'''
Vanya and Vova are playing a game. Players are given an integer 𝑛
. On their turn, the player can add 1
 to the current integer or subtract 1
. The players take turns; Vanya starts. If after Vanya's move the integer is divisible by 3
, then he wins. If 10
 moves have passed and Vanya has not won, then Vova wins.
'''

def helper(num):
    if num%3 == 0:
        return "Second"
    elif num%3 == 1 or num%3 ==2:
        return "First"


n = int(input()) #enter number of testcases 
for _ in range(n):
    num = int(input())
    print(helper(num))


