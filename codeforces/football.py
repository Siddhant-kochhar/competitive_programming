
s = input()

def check_dangerous(s):
    count = 1 
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
            if count >= 7:
                return "YES"
        else:
            count = 1 
    return "NO"

print(check_dangerous(s))
