s = "ABC $. def01ASDF"
s = "".join(s.split())
print(s.lower())

left = 0 
right = len(s) - 1
while left < right:
    if s[left].isalnum() and s[right].isalnum():
        if s[left].lower() != s[right].lower():
            print("Not a palindrome")
            break
        left += 1
        right -= 1
    elif not s[left].isalnum():
        left += 1
    elif not s[right].isalnum():
        right -= 1
else:
    print("Palindrome")